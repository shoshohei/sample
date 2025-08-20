#pragma once
#include "Actor.h"

class Ship :public Actor {
public:
	Ship(class Game* game);
	void ActorInput(const uint8_t* state) override;
	void UpdateActor(float deltaTime)override;
private:
	float mLaserCoolDown;
	class CircleComponent* mCircle;
};