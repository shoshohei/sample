#include "SquareComponent.h"
#include "Paddle.h"
#include "MoveComponent.h"
#include "SDL/SDL.h"

Paddle::Paddle(class Game* game)
	:Actor(game)
	,mSpeed(50.0f)
	,mDir(0)
{
	mSquare = new SquareComponent(this);
	//MoveComponent* mv = new MoveComponent(this);
	//mv->SetForwardSpeed(100.0f);
}

void Paddle::UpdateActor(float deltaTime) {
	Vector2 pos = GetPosition();
	pos.x += mSpeed * mDir * deltaTime;
	SetPosition(pos);
}

void Paddle::ActorInput(const uint8_t* key_state) {
	if (key_state[SDL_SCANCODE_A]) {
		mDir = 1;
	}
	else if (key_state[SDL_SCANCODE_D]) {
		mDir = -1;
	}
	else {
		mDir = 0;
	}
}