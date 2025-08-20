#include "InputComponent.h"
#include "Actor.h"

InputComponent::InputComponent(Actor* owner)
	:MoveComponent(owner)
	, mMaxAngularSpeed(0.0f)
	, mMaxForwardSpeed(0.0f)
	, mForwardKey(0)
	, mBackKey(0)
	, mClockwiseKey(0)
	, mCounterClockwiseKey(0)
{
}

void InputComponent::ProcessInput(const uint8_t* state) {
	if (mOwner->GetState() == Actor::EACTIVE) {
		float forwardSpeed = 0.0f;
		if (state[mForwardKey]) {
			forwardSpeed += mMaxForwardSpeed;
		}
		if (state[mBackKey]) {
			forwardSpeed -= mMaxForwardSpeed;
		}
		SetForwardspeed(forwardSpeed);
		AddForce(mOwner->GetForward() * forwardSpeed);

		float angularSpeed = 0.0f;
		if (state[mClockwiseKey]) {
			angularSpeed += mMaxAngularSpeed;
		}
		if (state[mCounterClockwiseKey]) {
			angularSpeed -= mMaxAngularSpeed;
		}
		SetAngularSpeed(angularSpeed);
	}
};