using System.Collections;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using Unity.VisualScripting;
using UnityEditor.Animations;
using UnityEngine;

public class minoController : MonoBehaviour
{
    public static minoController instance; 
    private Rigidbody rig;
    public string blockStatus;
    private Vector3 pre_pos;
    public int mino_id;
    /*
     * 1_T
     * 2_l
     */
    private Vector2 last_pos;
    private Transform[] children;
    public int child_num = 0;
    private Vector3 startPos;
    public int collision_count = 0;
    public float falling_count;
    private GameObject block_parent;

    // Start is called before the first frame update
    void Start()
    {
        instance = this;
        rig = GetComponent<Rigidbody>();
        rig.constraints = RigidbodyConstraints.FreezePosition
        | RigidbodyConstraints.FreezeRotation;
        blockStatus = "focus";
        children = GetComponentsInChildren<Transform>();
        foreach (Transform child in children)
        {
            if (child != transform)
            {
                child_num += 1;
            }
        }
        startPos = transform.position;
        block_parent = GameObject.FindWithTag("block_parent");
        if(GameManager.instance.dimension==3) transform.Rotate(new Vector3(90f, 0f, 0f));
    }

    // Update is called once per frame
    void Update()
    {
        if (blockStatus == "focus" || blockStatus == "fall")
        {
            if (Input.GetKeyDown(KeyCode.W))
            {
                pre_pos = transform.position;
                Vector3 new_pos = transform.position;
                new_pos.z += 1f;

                int res = 0;
                foreach (Transform child in children)
                {
                    Vector3 pos = child.transform.position;
                    pos.z += 1;
                    if (check_col(pos))
                        res++;
                }
                if (res == 0)
                    transform.position = new_pos;

            }
            else if (Input.GetKeyDown(KeyCode.S))
            {
                pre_pos = transform.position;
                Vector3 new_pos = transform.position;
                new_pos.z -= 1f;

                int res = 0;
                foreach (Transform child in children)
                {
                    Vector3 pos = child.transform.position;
                    pos.z -= 1;
                    if(check_col(pos))
                        res++;
                }
                if(res == 0)
                    transform.position = new_pos; 
            }
            else if (Input.GetKeyDown(KeyCode.A))
            {
                pre_pos = transform.position;
                Vector3 new_pos = transform.position;
                new_pos.x -= 1f;

                int res = 0;
                foreach (Transform child in children)
                {
                    Vector3 pos = child.transform.position;
                    pos.x -= 1;
                    if (check_col(pos))
                        res++;
                }
                if (res == 0)
                    transform.position = new_pos;
            }
            else if (Input.GetKeyDown(KeyCode.D))
            {
                pre_pos = transform.position;
                Vector3 new_pos = transform.position;
                new_pos.x += 1f;

                int res = 0;
                foreach (Transform child in children)
                {
                    Vector3 pos = child.transform.position;
                    pos.x += 1;
                    if (check_col(pos))
                        res++;
                }
                if (res == 0)
                    transform.position = new_pos;
            }

            if (GameManager.instance.focusblock_Status == "hold")
            {
                //holdする
                if (Input.GetKeyDown(KeyCode.H))
                {
                    float y = transform.position.y;
                    transform.position = new Vector3(0f, -10f, 0f);
                    GameManager.instance.change_hold(mino_id, y);
                    Destroy(gameObject);
                }
                //回転
                if (Input.GetKeyDown(KeyCode.Z))
                {
                    transform.Rotate(new Vector3(0f, 90f, 0f));
                }
                else if (Input.GetKeyDown(KeyCode.X))
                {
                    transform.Rotate(new Vector3(0f, 0f, 90f));
                }

                if (Input.GetKeyDown(KeyCode.Return))
                {
                    rig.constraints = RigidbodyConstraints.FreezeAll;


                    GameManager.instance.focusblock_Status = "fall";
                    foreach(Transform child in transform)
                    {
                        if (child != transform)
                        {
                            //child.AddComponent<Rigidbody>();
                            Rigidbody rig_child = child.GetComponent<Rigidbody>();
                            rig_child.constraints = RigidbodyConstraints.FreezeAll;
                            rig.useGravity = false;
                        }
                    }

                }
            }

            if (GameManager.instance.focusblock_Status == "fall")
            {
                if (falling_count < 0f)
                {
                    Vector3 pos = transform.position;
                    pos.y = pos.y - 1f;
                    transform.position = pos;
                    falling_count = 0.05f;
                }
                else
                {
                    falling_count -= Time.deltaTime;
                }
            }


            if (GameManager.instance.focusblock_Status == "hold")
            {
                if(falling_count < 0f)
                {
                    Vector3 pos = transform.position;
                    pos.y = pos.y-1f;
                    transform.position = pos;
                    falling_count = GameManager.instance.fall_interval;
                }
                else
                {
                    falling_count -= Time.deltaTime;
                }
            }

            
        }
    }

    private void OnCollisionEnter(Collision collision)
    {

        if (collision.gameObject.tag == "flat")
        {
            if (blockStatus == "hold")
            {
                GameManager.instance.gameStatus = "GameOver";
            }
            else
            {
                //int res = 0;
                //foreach(ContactPoint contact in collision.contacts)
                //{
                //    res++;
                //    print($"{contact.point},{contact.normal}");
                //}
                //print(res);
                int count = 0;
                foreach (ContactPoint contanct in collision.contacts)
                {
                    if (contanct.normal.y > 0.5f) //0fやと法線ベクトルのyが1.1E-17の可能性がありうまいこといかん
                    {
                        

                        //print($"{contanct.normal}, {contanct.normal.y}");
                        minoController.instance.blockStatus = "";
                        GameManager.instance.focusblock_Status = "interval";
                        child_fix_and_parent_Destroy();
                        break;
                    }
                    else
                    {
                        count++;
                    }
                }
            }
        }

        if (collision.gameObject.tag == "limit_bar")
        {
            transform.position = new Vector3(0f, transform.position.y, 0f); ;
        }
    }

    private void OnCollisionStay(Collision collision)
    {
        if(collision.gameObject.tag == "flat")
        {
            if(blockStatus != "hold")
            {
                int count = 0;
                foreach (ContactPoint contanct in collision.contacts)
                {
                    if (contanct.normal.y > 0.5f)
                    {
                        break;
                    }
                    else
                    {
                        count++;
                    }
                }
                
            }
        }
    }

    public void child_fix_and_parent_Destroy()
    {
        foreach(Transform child in children)
        {
            if (child != transform)
            {
                Rigidbody rig_child = child.GetComponent<Rigidbody>();
                SphereCollider col = rig_child.GetComponent<SphereCollider>();
                rig_child.constraints = RigidbodyConstraints.FreezeAll;
                child.SetParent(null);
                child.transform.SetParent(block_parent.transform);
                rig_child.isKinematic = false;
                if(child.transform.position.y > 20f)
                {
                    GameManager.instance.gameStatus = "GAMEOVER";
                    break;
                }
                GameManager.instance.Change_blockArray(child.transform.position);
                child.tag = "flat";
            }
        }
        Destroy(gameObject);
    }

    private bool check_col(Vector3 pos)
    {
        Collider[] col = Physics.OverlapSphere(pos, 0.1f);
        foreach(Collider c in col)
        {
            if(c.gameObject.tag == "flat")
                return true;
        }
        return false;
    }
}
