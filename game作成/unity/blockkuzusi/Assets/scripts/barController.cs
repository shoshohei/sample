using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;
using System.Collections.Generic;
public class barController : MonoBehaviour
{
    public barController instance;
    private Rigidbody rig;
    private float speed;
    public GameObject wall;
    private float wall_x;
    private float width_x;
    public Dictionary<int, float> mItemId_and_Time = new Dictionary<int, float>();
    private Vector3 normal_scale;
    public GameObject ballPrefab;
    public GameObject coverPrefab;
    public bool isStick;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        instance = this;
        rig = GetComponent<Rigidbody>();
        speed = 20f;
        wall_x = wall.transform.position.x;
        width_x = transform.localScale.x/2;
        normal_scale = transform.localScale;

        for(int i=0;i<GameManager.instance.GetItemNum();i++) mItemId_and_Time.Add(i, -1f);
        isStick = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.A))
        {
            //rig.linearVelocity = Vector3.right * -10f;
            if(transform.position.x >=-wall_x+width_x) 
                transform.Translate(Vector3.right * -speed * Time.deltaTime);
        }
        else if (Input.GetKey(KeyCode.D))
        {
            //rig.linearVelocity = Vector3.right * 10f;
            if (transform.position.x <= wall_x-width_x)
                transform.Translate(Vector3.right * speed * Time.deltaTime);
        }
        for (int i = 0; i< mItemId_and_Time.Count;i++)
        {
            if (mItemId_and_Time[i] > 0f)
            {
                mItemId_and_Time[i] -= Time.deltaTime;
            }
            else if (mItemId_and_Time[i]>-1f)
            {
                mItemId_and_Time[i] = -1f;
                if (i == 0)
                {
                    Vector3 scale = normal_scale;
                    scale.x = scale.x*2/3;
                    transform.localScale = scale;
                }
                else if (i == 2)
                {
                    coverPrefab.SetActive(false);
                    isStick = false;
                }
            }
        }
    }

    public bool GetIsStick() { return isStick; }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "item")
        {
            int id = other.gameObject.GetComponent<itemController>().instance.id;
            if (id == 0)
            {
                if (mItemId_and_Time[0] < 0f)
                {
                    Vector3 scale = normal_scale;
                    scale.x *= 1.5f;
                    transform.localScale = scale;
                }
                mItemId_and_Time[0] = 10f;
            }

            else if (id == 1)
            {
                GameObject obj = Instantiate(ballPrefab);
                obj.transform.position = new Vector3(0f, 8f, 0f);
            }

            else if (id == 2)
            {
                mItemId_and_Time[2] = 10f;
                coverPrefab.SetActive(true);
                isStick = true;
            }

            Destroy(other.gameObject);
        }

    }
}
