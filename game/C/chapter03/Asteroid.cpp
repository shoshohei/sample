#include "Asteroid.h"
#include "Game.h"
#include "Actor.h"
#include "Random.h"
#include "SpriteComponent.h"
#include "MoveComponent.h"
#include "CircleComponent.h"

Asteroid::Asteroid(Game* game)
	:Actor(game)
	,mCircle(nullptr)
{
	Vector2 pos = Random::GetVector(Vector2::Zero, Vector2(1024.0f, 768.0f));
	SetPosition(pos);
	SetRotation(Random::GetFloatRange(0.0f, Math::TwoPi));

	SpriteComponent* sc = new SpriteComponent(this);
	sc->SetTexture(game->GetTexture("Assets/Asteroid.png"));
	MoveComponent* mc = new MoveComponent(this);
	mc->SetForwardspeed(150.0f);
	mc->SetConstForce(Random::GetVector(Vector2(-10000.0f, -10000.0f), Vector2(10000.0f, 10000.0f)));
	mCircle = new CircleComponent(this);
	mCircle->SetRadius(40.0f);

	game->AddAsteroid(this);
}

Asteroid::~Asteroid() {
	GetGame()->RemoveAsteroid(this);
}