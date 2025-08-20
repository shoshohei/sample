using UnityEngine;

public class MoveBlockController : blockController
{
    private float mMoveRange;
    private float mMoveSpeed;
    private int mMoveAxis;
    private Vector3 mDefaultPosition;
    private float mMoveDirection;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    protected override void Start()
    {
        mDefaultPosition = transform.position;
        mMoveAxis = Random.Range(0, 3);
        mMoveAxis = 0;
        mMoveDirection = 1;
        mMoveRange = 5f;
        mMoveSpeed = 1f;

        if (mMoveAxis == 0)
        {
            rig.constraints = RigidbodyConstraints.FreezeRotation
                            | RigidbodyConstraints.FreezeRotationY
                            | RigidbodyConstraints.FreezeRotationZ;
        }
        else if (mMoveAxis == 1)
        {

            rig.constraints = RigidbodyConstraints.FreezeRotation
                            | RigidbodyConstraints.FreezeRotationX
                            | RigidbodyConstraints.FreezeRotationZ;
        }
        else if(mMoveAxis == 2)
        {
            rig.constraints = RigidbodyConstraints.FreezeRotation
                            | RigidbodyConstraints.FreezeRotationY
                            | RigidbodyConstraints.FreezeRotationX;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position[mMoveAxis] > mDefaultPosition[mMoveAxis] + mMoveRange ||
            transform.position[mMoveAxis] < mDefaultPosition[mMoveAxis] - mMoveRange)
        {
            mMoveDirection *= -1;
        }

        Vector3 pos = transform.position;
        pos[mMoveAxis] += mMoveDirection * mMoveSpeed * Time.deltaTime;
        transform.position = pos;
    }
}
