#pragma once
#include <vector>
#include "Math.h"
class Actor {
public:
	enum State {
		EACTIVE,
		EPAUSED,
		EDEAD
	};
	Actor(class Game* game);
	virtual ~Actor();

	void Update(float deltaTime);
	void UpdateComponents(float deltaTime);
	virtual void UpdateActor(float deltaTime);
	void ProcessInput(const uint8_t* keyState);
	virtual void ActorInput(const uint8_t* keyState);

	State GetState() const { return mState; };
	void SetState(State state) { mState = state; };
	Vector2 GetPosition() const { return mPosition; };
	void SetPosition(Vector2& pos) { mPosition = pos; };
	float GetScale() const { return mScale; };
	void SetScale(float scale) { mScale = scale; };
	float GetRotation()const { return mRotation; };
	void SetRotation(float rotate) { mRotation = rotate; };
	class Game* GetGame() { return mGame; };
	Vector2 GetForward() const { return Vector2(Math::Cos(mRotation), -Math::Sin(mRotation)); };
	void SetPausedTime(float time) {mPausedTime=time; };

	void AddComponent(class Component* component);
	void RemoveComponent(class Component* component);

private:
	State mState;
	Vector2 mPosition;
	float mScale;
	float mRotation;
	std::vector<class Component*> mComponents;
	class Game* mGame;
	float mPausedTime;
};