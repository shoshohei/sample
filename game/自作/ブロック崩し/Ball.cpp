#include "Ball.h"
#include "CircleComponent.h"
#include "game.h"
#include "Actor.h"
#include "SquareComponent.h"
#include "Block.h"
#include "Paddle.h"

Ball::Ball(class Game* game)
	:Actor(game)
{
	mCircle = new CircleComponent(this);
	mCircle->SetRadius(5.0f);
}

void Ball::UpdateActor(float deltaTime) {
	for (auto block : GetGame()->GetBlocks()) {
		if (Intersect(*(block->GetSquare()), *mCircle)) {
			block->SetState(EDead);
			Vector2 reflectDir = ReflectWithBlock(GetPosition(), block->GetPosition());
			Vector2 rot = Vector2(Math::Cos(GetRotation()), -Math::Sin(GetRotation()));
			Vector2 changerot = Vector2::Reflect(rot, reflectDir);
			SetRotation(changerot.y / changerot.x);
			break;
		}
	}

	Paddle* paddle = GetGame()->GetPaddle();
	if (Intersect(paddle->GetSquare(), *mCircle)) {
		Vector2 reflectDir = ReflectWithBlock(GetPosition(), paddle->GetPosition());
		Vector2 rot = Vector2(Math::Cos(GetRotation()), -Math::Sin(GetRotation()));
		Vector2 changerot = Vector2::Reflect(rot, reflectDir);
		SetRotation(changerot.y / changerot.x);
	}
}

Vector2& Ball::ReflectWithBlock(Vector2 ball, Vector2 block) {
	Vector2 normal = Vector2::Zero;
	float dx = (ball.x - block.x)/(block.x);
	float dy = (ball.y - block.y)/(block.y);
	if (fabs(dx) > fabs(dy)) {
		if (dx > 0) normal = Vector2::UnitX;
		else normal = Vector2::NegUnitX;
	}
	else {
		if (dy > 0) normal = Vector2::UnitY;
		else normal = Vector2::NegUnitY;
	}

	return normal;
}