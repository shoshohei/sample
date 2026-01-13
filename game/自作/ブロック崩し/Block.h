#pragma once
#include "Actor.h"

class Block : public Actor {
public:
	Block(class Game* game);
	void UpdateActor(float deltaTime) override;
	class SquareComponent* GetSquare() { return mSquare; }

private:
	int mHitPoint=1;
	class SquareComponent* mSquare;
};