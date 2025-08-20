using UnityEngine;

public class blockController : MonoBehaviour
{
    private Rigidbody rig;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        rig = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    //    public void OnCollisionEnter(Collision collision)
    //    {
    //        print("col in");
    //        if (collision.gameObject.tag == "flat" || collision.gameObject.tag == "part")
    //        {
    //            rig.linearVelocity = Vector3.zero;
    //        }
    //    }


}
