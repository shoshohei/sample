#include "AIState.h"
#include "AIComponent.h"
#include <SDL/SDL_log.h>
#include "Actor.h"
#include "Game.h"
#include "Tile.h"
#include "Grid.h"
#include "Enemy.h"
#include "Tower.h"
#include "Bullet.h"

void AIPatrol::Update(float deltaTime) {
	SDL_Log("update %s state", GetName());
	bool dead = true;
	if (dead) {
		mOwner->ChangeState("Death");
	}
}

void AIMove::Update(float deltaTime) {
	Actor* actor = mOwner->GetOwner();
	Vector2 diff = actor->GetPosition() - actor->GetGame()->GetGrid()->GetEndTile()->GetPosition();
	if (Math::NearZero(diff.Length(), 10.0f)) {
		mOwner->ChangeState("Death");
	}
}

void AIDeath::Update(float deltaTime) {
	mOwner->GetOwner()->SetState(Actor::EDead);
}

void AISerch::Update(float deltaTIme) {
	Actor* actor = mOwner->GetOwner();
	Enemy* e = actor->GetGame()->GetNearestEnemy(actor->GetPosition());
	if (e != nullptr) {
		Vector2 dir = e->GetPosition() - mTower->GetPosition();
		float dist = dir.Length();
		if (dist < mTower->GetAttackRange() && mTower->GetNextAttack()<0.0f) {
			mTower->SetTarget(e);
			mOwner->ChangeState("LookOn");
		}
	}
}

void AILookOn::Update(float deltaTime) {
	Enemy* e = mTower->GetTarget();
	if (e == nullptr) {
		mTower->SetTarget(nullptr);
		mOwner->ChangeState("Serch");
	}
	else {
		Vector2 dir = e->GetPosition() - mTower->GetPosition();
		float dist = dir.Length();
		mTower->SetRotation(Math::Atan2(-dir.y, dir.x));

		if (dist > mTower->GetAttackRange()) {
			mTower->SetTarget(nullptr);
			mOwner->ChangeState("Serch");
		}
		else {
			mOwner->ChangeState("Fire");
		}
	}
}

void AIFire::Update(float deltaTime) {
	Enemy* e = mTower->GetTarget();
	if (e == nullptr) {
		mOwner->ChangeState("Serch");
	}
	else {
		Bullet* b = new Bullet(mTower->GetGame());
		b->SetPosition(mTower->GetPosition());
		b->SetRotation(mTower->GetRotation());
		mOwner->ChangeState("Serch");
		mTower->SetNextAttack();
	}
}

void AIPatrol::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AIPatrol::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AIAttack::Update(float deltaTime)
{
	SDL_Log("Updating %s state", GetName());
}

void AIAttack::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AIAttack::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AIMove::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AIMove::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AIDeath::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AIDeath::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AISerch::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AISerch::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AILookOn::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AILookOn::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}

void AIFire::OnEnter()
{
	SDL_Log("Entering %s state", GetName());
}

void AIFire::OnExit()
{
	SDL_Log("Exiting %s state", GetName());
}
