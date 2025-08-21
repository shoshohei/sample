#pragma once
#include "Actor.h"

class Tower : public Actor
{
public:
	Tower(class Game* game);
	void UpdateActor(float deltaTime) override;
	void SetTarget(class Enemy* target) { mTarget = target; };
	class Enemy* GetTarget() { return mTarget; };
	const float GetAttackRange() const { return AttackRange; };
	void SetNextAttack() { mNextAttack = AttackTime; };
	float GetNextAttack() const { return mNextAttack; };
private:
	class MoveComponent* mMove;
	float mNextAttack;
	const float AttackTime = 2.5f;
	const float AttackRange = 100.0f;
	class Enemy* mTarget;
};
