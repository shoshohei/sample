#pragma once
#include "Component.h"
#include "Math.h"
#include "CircleComponent.h"

class SquareComponent : public Component {
public:
	SquareComponent(class Actor* owner);
	float SetXSize(float size) { mSize.x = size; }
	float SetYSize(float size) { mSize.y = size; }
	const Vector2& GetCenter()const;
	const Vector2& GetSize() const;
private:
	Vector2 mSize;
};

bool Intersect(const SquareComponent& a, const SquareComponent& b);
bool Intersect(const SquareComponent& a, const CircleComponent& b);