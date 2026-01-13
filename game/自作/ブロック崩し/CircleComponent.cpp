// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#include "CircleComponent.h"
#include "Actor.h"

CircleComponent::CircleComponent(class Actor* owner)
:Component(owner)
,mRadius(0.0f)
{
	
}

const Vector2& CircleComponent::GetCenter() const
{
	return mOwner->GetPosition();
}

float CircleComponent::GetRadius() const
{
	return mOwner->GetScale() * mRadius;
}

bool Intersect(const CircleComponent& a, const CircleComponent& b)
{
	// Calculate distance squared
	Vector2 diff = a.GetCenter() - b.GetCenter();
	float distSq = diff.LengthSq();

	// Calculate sum of radii squared
	float radiiSq = a.GetRadius() + b.GetRadius();
	radiiSq *= radiiSq;

	return distSq <= radiiSq;
}

//bool Intersect(const SquareComponent& a, const CircleComponent& b) {
//	Vector2 a_min = a.GetCenter() - a.GetSize();
//	Vector2 a_max = a.GetCenter() + a.GetSize();
//	Vector2 c = b.GetCenter();
//	Vector2 n;
//	n.x = std::max(a_min.x, std::min(c.x, a_max.x));
//	n.y = std::max(a_min.y, std::min(c.y, a_max.y));
//	Vector2 d = c - n;
//	float dist = d.Length();
//	return dist <= b.GetRadius();
//}