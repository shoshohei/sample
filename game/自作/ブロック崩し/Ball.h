#pragma once
#include "Actor.h"

class Ball :public Actor {
public:
	Ball(class Game* game);
	void UpdateActor(float deltaTime) override;
	class CircleComponent* GetCircle() { return mCircle; }
	Vector2& ReflectWithBlock(Vector2 ball, Vector2 block);
private:
	class CircleComponent* mCircle;
};