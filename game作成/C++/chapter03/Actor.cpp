#include "Actor.h"
#include "Game.h"
#include "Component.h"

Actor::Actor(class Game* game)
	:mGame(game)
	, mScale(1.0f)
	, mRotation(0.0f)
	, mPosition(Vector2::Zero)
	, mState(EACTIVE)
	,mPausedTime(1.5f)
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
	if (mState == EACTIVE) {
		UpdateComponents(deltaTime);
		UpdateActor(deltaTime);
	}
	if (GetState() == EPAUSED) {
		if (mPausedTime < 0.0f) {
			SetPosition(Vector2(GetGame()->GetWindowsWidth() / 2.0f, GetGame()->GetWindowHeight() / 2.0f));
			SetRotation(Math::PiOver2);
			printf("up\n");
			SetState(EACTIVE);
		}
		else {
			mPausedTime -= deltaTime;
		}
	}
}

void Actor::UpdateComponents(float deltaTime) {
	for (auto comp : mComponents) {
		comp->Update(deltaTime);
	}
}

void Actor::UpdateActor(float deltaTime) {

}

void Actor::ProcessInput(const uint8_t* keyState)
{
	if (mState == EACTIVE)
	{
		for (auto comp : mComponents)
		{
			comp->ProcessInput(keyState);
		}

		ActorInput(keyState);
	}
}

void Actor::ActorInput(const uint8_t* keyState)
{
}


void Actor::AddComponent(Component* comp) {
	int myOrder = comp->GetUpdateOrder();
	auto iter = mComponents.begin();
	for (;iter != mComponents.end();++iter) {
		if (myOrder < (*iter)->GetUpdateOrder())
			break;
	}
	mComponents.insert(iter, comp);
}

void Actor::RemoveComponent(Component* comp) {
	auto iter = std::find(mComponents.begin(), mComponents.end(), comp);
	if (iter != mComponents.end()) {
		mComponents.erase(iter);
	}
}