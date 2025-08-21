#include "Laser.h"
#include "Game.h"
#include "CircleComponent.h"
#include "MoveComponent.h"
#include "SpriteComponent.h"
#include "Asteroid.h"
#include "Actor.h"
#include "Component.h"

Laser::Laser(Game* game, float rotate)
	:Actor(game)
	,mDeathTimer(1.0f)
{
	SpriteComponent* sc = new SpriteComponent(this);
	sc->SetTexture(game->GetTexture("Assets/Laser.png"));
	MoveComponent* mc = new MoveComponent(this);
	mc->SetForwardspeed(800.0f);
	mc->SetConstForce(Vector2(Math::Cos(rotate)*1e5, -Math::Sin(rotate)*1e5));
	mCircle = new CircleComponent(this);
	mCircle->SetRadius(11.0f);
}

void Laser::UpdateActor(float deltaTime) {
	
	mDeathTimer -= deltaTime;
	if (mDeathTimer <= 0.0f) {
		SetState(EDEAD);
	}
	else {
		for (auto ast : GetGame()->GetAsteroids()) {
			if (Intersect(*mCircle, *(ast->GetCircle()))) {
				SetState(EDEAD);
				ast->SetState(EDEAD);
				break;
			}
		}
	}
}