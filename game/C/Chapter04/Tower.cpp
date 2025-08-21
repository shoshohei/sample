// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#include "Tower.h"
#include "SpriteComponent.h"
#include "MoveComponent.h"
#include "Game.h"
#include "Enemy.h"
#include "Bullet.h"
#include "AIComponent.h"
#include "AIState.h"

Tower::Tower(class Game* game)
	:Actor(game)
	,mTarget(nullptr)
{
	game->GetTowers().emplace_back(this);
	SpriteComponent* sc = new SpriteComponent(this, 200);
	sc->SetTexture(game->GetTexture("Assets/Tower.png"));

	mMove = new MoveComponent(this);

	AIComponent* aic = new AIComponent(this);
	aic->RegisterState(new AILookOn(aic, this));
	aic->RegisterState(new AIFire(aic, this));
	aic->RegisterState(new AISerch(aic, this));
	aic->ChangeState("Serch");
	mNextAttack = AttackTime;
}

void Tower::UpdateActor(float deltaTime)
{
	Actor::UpdateActor(deltaTime);

	mNextAttack -= deltaTime;
	
}
