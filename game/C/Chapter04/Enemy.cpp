#include "Enemy.h"
#include "Game.h"
#include "SpriteComponent.h"
#include "NavComponent.h"
#include "Grid.h"
#include "Tile.h"
#include "CircleComponent.h"
#include <algorithm>
#include "AIComponent.h"
#include "AIState.h"
#include "Tower.h"

Enemy::Enemy(Game* game)
	:Actor(game) {
	game->GetEnemies().emplace_back(this);

	SpriteComponent* sc = new SpriteComponent(this);
	sc->SetTexture(game->GetTexture("Assets/Airplane.png"));

	SetPosition(GetGame()->GetGrid()->GetStartTile()->GetPosition());
	// Setup a nav component at the start tile
	NavComponent* nc = new NavComponent(this);
	nc->SetForwardSpeed(150.0f);
	nc->StartPath(GetGame()->GetGrid()->GetStartTile());

	AIComponent* aic = new AIComponent(this);
	aic->RegisterState(new AIDeath(aic));
	aic->RegisterState(new AIMove(aic));
	aic->ChangeState("Move");

	mCircle = new CircleComponent(this);
	mCircle->SetRadius(25.0f);
}

Enemy::~Enemy() {
	//Tower‚ÌmTarget‚©‚çœŠO
	std::vector<Tower*> towers = GetGame()->GetTowers();
	for(auto tower : towers)
	{
		Enemy* target = tower->GetTarget();
		if (target == this) {
			tower->SetTarget(nullptr);
		}
	}

	auto iter = std::find(GetGame()->GetEnemies().begin(),
		GetGame()->GetEnemies().end(), this);
	GetGame()->GetEnemies().erase(iter);
}

void Enemy::UpdateActor(float deltaTime) {
	Actor::UpdateActor(deltaTime);
}