#include "Actor.h"
#include "Game.h"
#include "Component.h"
#include <algorithm>

Actor::Actor(Game* game)
	:mState(EActive)
	, mPosition(Vector2(0.0f, 0.0f))
	, mScale(1.0f)
	, mRotation(0.0f)
	, mGame(game)
{
	mGame->AddActor(this);
}

Actor::~Actor() {
	mGame->RemoveActor(this);
	while (!mComponents.empty()) {
		delete mComponents.back();
	}
}

void Actor::Update(float deltaTime) {
	if (mState == EActive) {
		UpdateComponents(deltaTime);
		UpdateActor(deltaTime);
	}
}

void Actor::UpdateComponents(float deltaTime) {
	for (auto comp : mComponents) {
		comp->Update(deltaTime);
	}
}

void Actor::UpdateActor(float deltaTime) {};

void Actor::ProcessInput(const uint8_t* keystate) {
	if (mState == EActive) {
		for (auto comp : mComponents) {
			comp->ProcessInput(keystate);
		}
		ActorInput(keystate);
	}
}

void Actor::ActorInput(const uint8_t* keystate) {};

void Actor::AddComponent(Component* comp) {
	int myOrder = comp->GetUpdateOrder();
	auto iter = mComponents.begin();
	for (;iter != mComponents.end();++iter) {
		if ((*iter)->GetUpdateOrder() > myOrder) {
			break;
		}
	}
	mComponents.insert(iter, comp);
}

void Actor::RemoveComponent(Component* comp) {
	auto iter = std::find(mComponents.begin(), mComponents.end(), comp);
	if (iter != mComponents.end()) {
		mComponents.erase(iter);
	}
}