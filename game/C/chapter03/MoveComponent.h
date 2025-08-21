#pragma once
#include "Component.h"
#include "Math.h"

class MoveComponent : public Component {
public:
	MoveComponent(class Actor* actor, int updateOrder = 10);
	void Update(float deltaTime) override;
	float GetAngularSpeed() const { return mAngularSpeed; };
	void SetAngularSpeed(float Speed) { mAngularSpeed = Speed; };
	float GetForwardSpeed() const { return mForwardSpeed; };
	void SetForwardspeed(float speed) { mForwardSpeed = speed; };
	void SetConstForce(const Vector2& force) { mConstForce = force; };
	void AddForce(const Vector2& force) { 
		mSumForce += force; 
	};

private:
	float mAngularSpeed;
	float mForwardSpeed;
	float mMass;
	Vector2 mSumForce;
	Vector2 mVelocity;
	Vector2 mConstForce;
};