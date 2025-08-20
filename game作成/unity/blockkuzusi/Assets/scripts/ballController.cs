using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;
public class ballController : MonoBehaviour
{
    public ballController instance;
    private Rigidbody rig;
    public Vector3 lastVelo;
    private GameObject barPrefab;
    private float velo_mag;
    public Vector3 velo;
    private float speed;
    private float pre_x;
    private float pre_z;
    public bool stick_on_bar=false;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        instance = this;
        barPrefab = GameObject.FindWithTag("bar");
        rig = GetComponent<Rigidbody>();
        speed = 15f;
        rig.linearVelocity = new Vector3(0f, -speed, 0f);
    }

    // Update is called once per frame
    void Update()
    {
        if(rig.linearVelocity.y < 0.01f && rig.linearVelocity.y > -0.01f)
        {
            rig.linearVelocity = new Vector3(-pre_x, -0.5f, -pre_z).normalized * speed;
        }
        //print("up");
        velo = rig.linearVelocity;
        //print(rig.linearVelocity);
        rig.linearVelocity = rig.linearVelocity.normalized* speed;
        if(rig.linearVelocity.magnitude > 0.1f)
        {
            pre_x = rig.linearVelocity.x;
            pre_z = rig.linearVelocity.z;
        }
        else if(rig.linearVelocity.magnitude <0.01f)
        {
            rig.linearVelocity = new Vector3(-pre_x, -1f, -pre_z).normalized* speed; 
        }
        if (transform.position.y < -10f)
        {
            Vector3 pos = new Vector3(0f, 8f, 0f);
            transform.position = pos;
            rig.linearVelocity = new Vector3(0f, -speed, 0f);
        }
        if(stick_on_bar && Input.GetKey(KeyCode.Return))
        {
            switch_stick();
            ball_fire();
        }
        

        if(GameManager.instance.gameStatus == "CLEAR"||GameManager.instance.gameStatus=="GAMEOVER")
        {
            Destroy(this.gameObject);
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "bar")
        {
            if (!collision.gameObject.GetComponent<barController>().instance.GetIsStick())
            {
                // barÇ∆ballÇ™ìñÇΩÇ¡ÇΩéûÇÃîΩéÀèàóù
                float pos_x = (this.transform.position.x - collision.gameObject.transform.position.x) / collision.gameObject.transform.localScale.x;
                rig.linearVelocity = new Vector3(pos_x, 1f, 0f).normalized * speed;
            }
            else
            {
                switch_stick();
                this.transform.SetParent(collision.gameObject.transform);
            }
        }
    }

    public void ball_fire()
    {
        rig.linearVelocity = new Vector3(0f, speed, 0f);
        this.transform.SetParent(null);
    }

    public bool switch_stick()
    {
        if (!stick_on_bar)
        {
            stick_on_bar = true;
            rig.isKinematic = true;
        }
        else
        {
            rig.isKinematic = false;
            stick_on_bar=false;
        }
        return stick_on_bar;
    }
}
