using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public static PlayerController instance;
    private Vector3 startPos;
    // Start is called before the first frame update
    void Start()
    {
        instance = this;
        Vector3 pos = transform.position;
        pos.y =  16;
        transform.position = pos;
        startPos = pos;
    }

    // Update is called once per frame
    void Update()
    {
        if (GameManager.instance.gameStatus == "PLAY")
        {
            if (Input.GetKey(KeyCode.Q))
            {
                transform.Rotate(new Vector3(0f, 2f, 0f));
            }
            if (Input.GetKey(KeyCode.E))
            {
                transform.Rotate(new Vector3(0f, -2f, 0f));
            }
        }
    }

    public void change_pos(float _y)
    {   
        Vector3 pos = startPos;
        pos.y += _y;
        transform.position = pos;
    }
}
