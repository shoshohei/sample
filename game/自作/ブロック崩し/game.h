#pragma once
#include "SDL/SDL.h"
#include <vector>
#include "Math.h"

//struct Vector2 {
//	float x;
//	float y;
//};



class Game {
public:
	Game();
	bool Initialize();
	void RunLoop();
	void Shutdown();

	void AddBlock(class Block* block);
	void RemoveBlock(class Block* block);
	std::vector<class Block*>& GetBlocks() { return mBlocks; }
	
	void AddBall(class Ball* ball);
	void RemoveBall(class Ball* ball);
	std::vector<class Ball*>& GetBalls() { return mBalls; }

	void AddActor(class Actor* actor);
	void RemoveActor(class Actor* actor);

	class Paddle* GetPaddle() const { return mPaddle; }

private:
	void ProcessInput();
	void UpdateGame();
	void GenerateOutput();
	SDL_Window* mWindow;
	bool mIsRunning;
	SDL_Renderer* mRenderer;
	Uint32 mTicksCount;
	int mBlockNumX=20;
	int mBlockNumY=5;

	std::vector<class Ball*> mBalls;
	std::vector<class Block*> mBlocks;
	class Paddle* mPaddle;
};