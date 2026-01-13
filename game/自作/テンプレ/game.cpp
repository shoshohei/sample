#include "game.h"

#include <random>
const int window_height = 768;
const int window_width = 1024;
std::random_device rd;
std::mt19937 gen(rd());
//std::uniform_real_distribution<> dist((window_width-bar_width)/2+tickness, (window_width + bar_width) / 2-tickness);

Game::Game()
	:mIsRunning(true)
	, mRenderer(nullptr)
	, mTicksCount(0)
{

}

bool Game::Initialize() {
	int sdlResult = SDL_Init(SDL_INIT_VIDEO);
	if (sdlResult != 0) {
		SDL_Log("‰Šú‰»‚Å‚«‚È‚©‚Á‚½D:%s", SDL_GetError());
		return false;
	}
	mWindow = SDL_CreateWindow(
		"first window",
		50, 50, window_width, window_height, 0
	);
	if (!mWindow) {
		SDL_Log("Windowì‚ê‚Ö‚ñ‚¾D:%s", SDL_GetError());
		return false;
	}
	mRenderer = SDL_CreateRenderer(
		mWindow,
		-1,
		SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
	);
	if (!mRenderer) {
		SDL_Log("RendererŽæ“¾‚Å‚«‚Ü‚¹‚ñ‚Å‚µ‚½D:%s", SDL_GetError());
		return false;
	}
	return true;
}

void Game::Shutdown() {
	SDL_DestroyWindow(mWindow);
	SDL_DestroyRenderer(mRenderer);
	SDL_Quit();
}

void Game::RunLoop() {
	while (mIsRunning) {
		ProcessInput();
		UpdateGame();
		GenerateOutput();
	}
}

void Game::ProcessInput() {
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type) {
		case SDL_QUIT:
			mIsRunning = false;
			break;
		default: break;
		}
	}
	
	const Uint8* state = SDL_GetKeyboardState(NULL);
	if (state[SDL_SCANCODE_ESCAPE])
		mIsRunning = false;

}

void Game::UpdateGame() {
	while(!SDL_TICKS_PASSED(SDL_GetTicks(), mTicksCount + 16));
	float deltaTime = (SDL_GetTicks() - mTicksCount) / 1000.0f;
	mTicksCount = SDL_GetTicks();
	if (deltaTime > 0.05f) {
		deltaTime = 0.05f;
	}
}

void Game::GenerateOutput() {
	//”wŒi‚Ì•`‰æ
	SDL_SetRenderDrawColor(
		mRenderer, 0, 0, 0, 255
	);
	SDL_RenderClear(mRenderer);
	
	
	
	SDL_RenderPresent(mRenderer);
}