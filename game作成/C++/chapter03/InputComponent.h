#pragma once
#include "MoveComponent.h"

class InputComponent :public MoveComponent {
public:
	InputComponent(class Actor* owner);
	void ProcessInput(const uint8_t* state) override;
	void SetMaxForwadSpeed(float speed) { mMaxForwardSpeed = speed; };
	void SetMaxAngularSpeed(float speed) { mMaxAngularSpeed = speed; };
	void SetForwardKey(int key) { mForwardKey = key; };
	void SetBackkey(int key) { mBackKey = key; };
	void SetClockwiseKey(int key) { mClockwiseKey = key; };
	void SetCounterClockwiseKey(int key) { mCounterClockwiseKey = key; };

private:
	float mMaxForwardSpeed;
	float mMaxAngularSpeed;
	
	int mForwardKey;
	int mBackKey;
	int mClockwiseKey;
	int mCounterClockwiseKey;
	
};