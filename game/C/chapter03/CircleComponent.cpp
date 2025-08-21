#include "CircleComponent.h"
#include "Actor.h"

CircleComponent::CircleComponent(Actor* owner)
	:Component(owner)
	, mRadius(0.0f)
{
}

float CircleComponent::GetRadius () const{
	return mOwner->GetScale() * mRadius;
}

const Vector2& CircleComponent::GetCenter()const {
	return mOwner->GetPosition();
}

bool Intersect(const CircleComponent& a, const CircleComponent& b) {
	//between centers dis
	Vector2 a_ = a.GetCenter();
	Vector2 b_ = b.GetCenter();
	Vector2 diff = a_-b_;
	float dis = diff.LengthSq();
	
	//sum radius
	float addRadius = a.GetRadius() + b.GetRadius();
	addRadius *= addRadius;

	return dis <= addRadius;
}