#include "Block.h"
#include "SquareComponent.h"
#include "game.h"
#include "Actor.h"
#include "CircleComponent.h"
#include "Ball.h"

Block::Block(Game* game)
	:Actor(game)
{
	mSquare = new SquareComponent(this);
	mSquare->SetXSize(1.0f);
	mSquare->SetYSize(1.0f);
}

void Block::UpdateActor(float deltaTime) {
	
}

