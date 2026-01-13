#pragma once
#include "Actor.h"

class Paddle :public Actor {
public:
	Paddle(class Game* game);
	void UpdateActor(float deltaTime) override;
	void ActorInput(const uint8_t* keyState) override;
	class SquareComponent* GetSquare() { return mSquare; }
private:
	class SquareComponent* mSquare;
	float mSpeed;
	int mDir;
};