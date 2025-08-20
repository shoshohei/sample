#include "MoveComponent.h"
#include "Actor.h"
#include "Component.h"
#include "Game.h"
#include "Random.h"

MoveComponent::MoveComponent(class Actor* actor, int updateOrder)
	:Component(actor, updateOrder)
	, mAngularSpeed(0.0f)
	, mForwardSpeed(0.0f)
	,mMass(1.0f)
	,mSumForce(Vector2::Zero)
	,mVelocity(Vector2::Zero)
{
}

void MoveComponent::Update(float deltaTime) {
	if (!Math::NearZero(mAngularSpeed)) {
		float rot = mOwner->GetRotation();
		rot += mAngularSpeed * deltaTime;
		mOwner->SetRotation(rot);
	}
	if (!Math::NearZero(mForwardSpeed)) {
		//Vector2 pos = mOwner->GetPosition();
		//pos += mForwardSpeed * deltaTime * mOwner->GetForward();
		
		
		AddForce(mConstForce);
		Vector2 Accelaration = Vector2(mSumForce.x/mMass, mSumForce.y/mMass);
		mSumForce = Vector2::Zero;
		mVelocity = Accelaration * deltaTime;
		Vector2 pos = mOwner->GetPosition();
		pos += mVelocity * deltaTime;

		if (pos.x > mOwner->GetGame()->GetWindowsWidth()) {
			pos.x -= mOwner->GetGame()->GetWindowsWidth();
		}
		else if (pos.x < 0.0f) {
			pos.x += mOwner->GetGame()->GetWindowsWidth();
		}
		if (pos.y > mOwner->GetGame()->GetWindowHeight()) {
			pos.y -= mOwner->GetGame()->GetWindowHeight();
		}
		else if (pos.y < 0.0f) {
			pos.y += mOwner->GetGame()->GetWindowHeight();
		}
		
		mOwner->SetPosition(pos);
	}
}