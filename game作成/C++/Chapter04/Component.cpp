#include "Component.h"
#include "Actor.h"

Component::Component(Actor* actor, int updateOrder)
	:mOwner(actor)
	, mUpdateOrder(updateOrder)
{
	mOwner->AddComponent(this);
}

Component::~Component() {
	mOwner->RemoveComponent(this);
}

void Component::Update(float deltaTime) {};

