#include "Ship.h"
#include "Game.h"
#include "InputComponent.h"
#include "SpriteComponent.h"
#include "Laser.h"
#include "CircleComponent.h"
#include "Asteroid.h"

Ship::Ship(Game* game)
	:Actor(game)
	,mLaserCoolDown(0.0f)
{
	SpriteComponent* sc = new SpriteComponent(this);
	sc->SetTexture(game->GetTexture("Assets/Ship.png"));

	InputComponent* ic = new InputComponent(this);
	ic->SetMaxAngularSpeed(Math::TwoPi);
	ic->SetMaxForwadSpeed(3e4);
	ic->SetForwardKey(SDL_SCANCODE_W);
	ic->SetBackkey(SDL_SCANCODE_S);
	ic->SetClockwiseKey(SDL_SCANCODE_D);
	ic->SetCounterClockwiseKey(SDL_SCANCODE_A);

	mCircle = new CircleComponent(this);
	mCircle->SetRadius(5.0f);
}

void Ship::UpdateActor(float deltaTime) {
	mLaserCoolDown -= deltaTime;
	for (auto ast : GetGame()->GetAsteroids()) {
		if (Intersect(*mCircle, *(ast->GetCircle()))) {
			SetPosition(Vector2(GetGame()->GetWindowsWidth() * 2.0f, GetGame()->GetWindowHeight() * 2.0f));
			SetPausedTime(1.5f);
			SetState(EPAUSED);
			break;
		}
	}
}

void Ship::ActorInput(const uint8_t* state) {
	if (state[SDL_SCANCODE_SPACE]&&mLaserCoolDown<=0.0f) {
		Laser* laser = new Laser(GetGame(), GetRotation());
		laser->SetPosition(GetPosition());
		laser->SetRotation(GetRotation());
		mLaserCoolDown = 0.5f;
	}
}