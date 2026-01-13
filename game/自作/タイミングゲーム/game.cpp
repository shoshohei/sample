#include "game.h"

const int tickness = 15;
const int window_width = 512;
const int window_height = 400;
const float paddleH = 100.0f;
const float paddle_velo = 300.0f;
const float ball_velo = 1.0f;
const float bar_width = 200.0f;
#include <random>
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_real_distribution<> dist((window_width-bar_width)/2+tickness, (window_width + bar_width) / 2-tickness);

Game::Game()
	:mIsRunning(true)
	, mRenderer(nullptr)
	, mTicksCount(0)
	, mPaddleDir(0)
	, mPaddleDir2(0)
	, player_Dir(1)
	, mState(ESelect)
	, player_bar(window_width/2)
{

}

bool Game::ball_out_of_window(Ball ball) {
	if (ball.pos.x < 0.0f || ball.pos.x > window_width ||
		ball.pos.y<0.0f || ball.pos.y>window_height) {
		return true;
	}
	return false;
}

bool Game::Initialize() {
	int sdlResult = SDL_Init(SDL_INIT_VIDEO);
	if (sdlResult != 0) {
		SDL_Log("èâä˙âªÇ≈Ç´Ç»Ç©Ç¡ÇΩÅD:%s", SDL_GetError());
		return false;
	}
	mWindow = SDL_CreateWindow(
		"first window",
		50, 50, window_width, window_height, 0
	);
	if (!mWindow) {
		SDL_Log("WindowçÏÇÍÇ÷ÇÒÇæÅD:%s", SDL_GetError());
		return false;
	}
	mRenderer = SDL_CreateRenderer(
		mWindow,
		-1,
		SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
	);
	if (!mRenderer) {
		SDL_Log("RendereréÊìæÇ≈Ç´Ç‹ÇπÇÒÇ≈ÇµÇΩÅD:%s", SDL_GetError());
		return false;
	}
	mPaddlePos.x = 10.0f;
	mPaddlePos.y = window_height / 2.0f;
	mPaddlePos2.x = window_width - mPaddlePos.x -tickness;
	mPaddlePos2.y = mPaddlePos.y;
	Ball ball1 = { {window_width / 2.0f, window_height / 2.0f}, {-200.0f, 235.0f} };
	Ball ball2 = { {window_width / 2.0f, window_height / 2.0f}, {200.0f, -235.0f} };
	balls.push_back(ball1);
	balls.push_back(ball2);
	/*int initialize_veloflg = 1;
	balls.resize(2);
	for (Ball ball : balls) {
		ball.pos.x = window_width / 2.0f;
		ball.pos.y = window_height / 2.0f;
		ball.velo.x = -200.0f;
		ball.velo.y = 235.0f*initialize_veloflg;
		initialize_veloflg *= -1;
	}*/
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
	//SDL_Log("in_process_input");
	
	const Uint8* state = SDL_GetKeyboardState(NULL);
	//SDL_Log("%d", state[SDL_SCANCODE_0]);
	if (state[SDL_SCANCODE_ESCAPE])
		mIsRunning = false;
	if (state[SDL_SCANCODE_SPACE]) {
		if (mState!=EClear && ((player_bar - correct_pos) <= tickness && (player_bar - correct_pos) >= -tickness)) {
			mState = EClear;

			SDL_Log("clear!\tscore:%.1f \t player:%f, correct:%f", player_bar - correct_pos, player_bar, correct_pos);
		}
	}
	if (state[SDL_SCANCODE_RETURN] && mState==EClear) {
		mState = ESelect;
	}

}

void Game::UpdateGame() {
	while(!SDL_TICKS_PASSED(SDL_GetTicks(), mTicksCount + 16));
	float deltaTime = (SDL_GetTicks() - mTicksCount) / 1000.0f;
	mTicksCount = SDL_GetTicks();
	if (deltaTime > 0.05f) {
		deltaTime = 0.05f;
	}
	//SDL_Log("mPaddleDir:%d\n", mPaddleDir);
	if (mState == ESelect) {
		correct_pos = dist(gen);
		mState = EMove;
	}
	
	if (mState!=EClear)
		player_bar += player_Dir * 150 * deltaTime;
	/*if (player_bar < 50 + tickness / 2 || window_width - 50 - tickness / 2 < player_bar) {
		player_Dir *= -1;
	}*/
	if (player_bar < (window_width - bar_width + tickness)/2 || (window_width + bar_width - tickness)/2<player_bar) {
		player_Dir *= -1;
	}
}

void Game::GenerateOutput() {
	//îwåiÇÃï`âÊ
	SDL_SetRenderDrawColor(
		mRenderer, 0, 0, 0, 255
	);
	SDL_RenderClear(mRenderer);
	
	SDL_SetRenderDrawColor(
		mRenderer, 0, 255, 255, 255
	);
	//è„ïîï«ÇÃï`âÊ
	SDL_Rect bar{
		(window_width-bar_width)/2, (window_height - tickness) / 2, bar_width, tickness
	};
	SDL_RenderFillRect(mRenderer, &bar);
	SDL_SetRenderDrawColor(
		mRenderer, 0, 0, 255, 255
	);
	SDL_Rect correct_bar{
		correct_pos-tickness/2, (window_height - tickness) / 2, tickness, tickness
	};
	SDL_RenderFillRect(mRenderer, &correct_bar);
	SDL_SetRenderDrawColor(
		mRenderer, 255, 0, 0, 255
	);
	SDL_Rect player{
		player_bar-tickness/2, (window_height - tickness) / 2, tickness, tickness
	};
	SDL_RenderFillRect(mRenderer, &player);

	////ballÇÃï`âÊ
	//for (Ball b : balls) {
	//	SDL_Rect ball{
	//	static_cast<int>(b.pos.x - tickness / 2),
	//	static_cast<int>(b.pos.y - tickness / 2),
	//	tickness, tickness
	//	};
	//	SDL_RenderFillRect(mRenderer, &ball);
	//}
	
	SDL_RenderPresent(mRenderer);
}