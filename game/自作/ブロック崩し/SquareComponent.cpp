#include "SquareComponent.h"
#include "Actor.h"

SquareComponent::SquareComponent(class Actor* owner)
:Component(owner)
,mSize(Vector2(0.0f, 0.0f))
{

}

const Vector2& SquareComponent::GetCenter() const {
	return mOwner->GetPosition();
}

const Vector2& SquareComponent::GetSize() const {
	return mOwner->GetScale() * mSize;;
}

bool Intersect(const SquareComponent& a, const SquareComponent& b) {
	Vector2 a_min = a.GetCenter() - a.GetSize();
	Vector2 a_max = a.GetCenter() + a.GetSize();
	Vector2 b_min = b.GetCenter() - b.GetSize();
	Vector2 b_max = b.GetCenter() + b.GetSize();

	if (a_max.x < b_min.x) return false;
	if (a_min.x > b_max.x) return false;
	if (a_max.y < b_min.y) return false;
	if (a_min.y > b_max.y) return false;
	return true;
}

bool Intersect(const SquareComponent& a, const CircleComponent& b) {
	Vector2 a_min = a.GetCenter() - a.GetSize();
	Vector2 a_max = a.GetCenter() + a.GetSize();
	Vector2 c = b.GetCenter();
	Vector2 n;
	n.x = std::max(a_min.x, std::min(c.x, a_max.x));
	n.y = std::max(a_min.y, std::min(c.y, a_max.y));
	Vector2 d = c - n;
	float dist = d.Length();
	return dist <= b.GetRadius();
}