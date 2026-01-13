#pragma once
#include "SDL/SDL.h"
#include <vector>


struct Vector2 {
	float x;
	float y;
};

struct Ball {
	Vector2 pos;
	Vector2 velo;
};

class Game {
public:
	enum GState {
		EMove,
		EFault,
		EClear,
		ESelect
	};
	Game();
	bool Initialize();
	void RunLoop();
	void Shutdown();
private:
	void ProcessInput();
	void UpdateGame();
	void GenerateOutput();
	bool ball_out_of_window(Ball ball);
	SDL_Window* mWindow;
	bool mIsRunning;
	SDL_Renderer* mRenderer;
	std::vector<Ball> balls;
	Vector2 mPaddlePos;
	Vector2 mPaddlePos2;
	Uint32 mTicksCount;
	int mPaddleDir;
	int mPaddleDir2;
	int player_Dir;
	float correct_pos;
	float player_bar;
	GState mState;
};