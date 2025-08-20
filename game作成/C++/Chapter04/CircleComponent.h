#pragma once
#include "Component.h"
#include "Math.h"

class CircleComponent :public Component {
public:
	CircleComponent(class Actor* actor);

	void SetRadius(float rot) { mRadius = rot; };
	float GetRadius()const;

	const Vector2& GetCenter() const;

private:
	float mRadius;
};

bool Intersect(const CircleComponent& a, const CircleComponent& b);