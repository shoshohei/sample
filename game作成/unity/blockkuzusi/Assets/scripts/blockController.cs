using UnityEngine;

public class blockController : MonoBehaviour
{
    public int hp;
    public bool mIsCountBlock;
    protected Rigidbody rig;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    protected virtual void Start()
    {
        rig = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    protected void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "ball")
        {
            hp--;
            if (hp <= 0)
            {
                if(mIsCountBlock) 
                    GameManager.instance.block_count--;
                GameManager.instance.Random_Item(transform.position);
                Destroy(gameObject);
            }
        }

    }
}
