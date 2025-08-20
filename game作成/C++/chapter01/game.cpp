#include "game.h"

const int tickness = 15;
const int window_width = 1024;
const int window_height = 768;
const float paddleH = 100.0f;
const float paddle_velo = 300.0f;
const float ball_velo = 1.0f;

Game::Game()
	:mIsRunning(true)
	, mRenderer(nullptr)
	, mTicksCount(0)
	, mPaddleDir(0)
	, mPaddleDir2(0)
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
		0, 0, window_width, window_height, 0
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
	mPaddleDir = 0;
	if (state[SDL_SCANCODE_W]) {
		mPaddleDir -= 1;
	}
	if (state[SDL_SCANCODE_S]) {
		mPaddleDir += 1;
	}
	mPaddleDir2 = 0;
	if (state[SDL_SCANCODE_I]) {
		mPaddleDir2 -= 1;
	}
	if (state[SDL_SCANCODE_K]) {
		mPaddleDir2 += 1;
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
	if (mPaddleDir != 0) {
		//SDL_Log("go:%f\n", mPaddleDir * 300.0f * deltaTime);
		mPaddlePos.y += mPaddleDir * paddle_velo * deltaTime;
		if (mPaddlePos.y < paddleH/2.0f + tickness) {
			mPaddlePos.y = paddleH/2.0f + tickness;
		}
		else if (mPaddlePos.y > window_height - tickness - paddleH / 2.0f) {
			mPaddlePos.y = window_height - tickness - paddleH/2.0f;
		}
	}
	if (mPaddleDir2 != 0) {
		//SDL_Log("go:%f\n", mPaddleDir * 300.0f * deltaTime);
		mPaddlePos2.y += mPaddleDir2 * paddle_velo * deltaTime;
		if (mPaddlePos2.y < paddleH / 2.0f + tickness) {
			mPaddlePos2.y = paddleH / 2.0f + tickness;
		}
		else if (mPaddlePos2.y > window_height - tickness - paddleH / 2.0f) {
			mPaddlePos2.y = window_height - tickness - paddleH / 2.0f;
		}
	}
	for (Ball &ball : balls) {
		//ballÇÃà⁄ìÆ
		ball.pos.x += ball.velo.x * deltaTime * ball_velo;
		ball.pos.y += ball.velo.y * deltaTime * ball_velo;
		//ï«è„ïîÇÃîΩéÀ
		if (ball.pos.y < tickness && ball.velo.y < 0.0f) {
			ball.velo.y *= -1;
		}
		//ï«â∫ïîÇÃîΩéÀ
		else if (ball.pos.y > window_height - tickness && ball.velo.y > 0.0f) {
			ball.velo.y *= -1;
		}
		//ÉpÉhÉãÇ∆ÇÃîΩéÀ
		float diff = mPaddlePos.y - ball.pos.y;
		diff = (diff > 0.0f) ? diff : -diff;
		if (
			diff < paddleH / 2.0f &&
			ball.pos.x <= mPaddlePos.x + tickness && ball.pos.x >= mPaddlePos.x + tickness - 2.5f &&
			ball.velo.x < 0.0f
			) {
			ball.velo.x *= -1;
		}
		float diff2 = mPaddlePos2.y - ball.pos.y;
		diff2 = (diff2 > 0.0f) ? diff2 : -diff2;
		if (
			diff2 < paddleH / 2.0f &&
			ball.pos.x >= mPaddlePos2.x - tickness / 2 && ball.pos.x <= mPaddlePos2.x + 2.5f - tickness / 2 &&
			ball.velo.x > 0.0f
			) {
			ball.velo.x *= -1;
		}
	}
	if (Game::ball_out_of_window(balls[0]) && Game::ball_out_of_window(balls[1])) {
		mIsRunning = false;
	}
	
	
	//ï«ç∂ïîÇÃîΩéÀ
	//else if (mBallPos.x < tickness && mBallVelo.x < 0.0f) {
	//	mBallVelo.x *= -1;
	//}
	//ï«âEïîÇÃîΩéÀ
	//else if (mBallPos.x > window_width - tickness && mBallVelo.x > 0.0f) {
	//	mBallVelo.x *= -1;
	//}
	
}

void Game::GenerateOutput() {
	//îwåiÇÃï`âÊ
	SDL_SetRenderDrawColor(
		mRenderer, 0, 0, 255, 255
	);
	SDL_RenderClear(mRenderer);
	
	SDL_SetRenderDrawColor(
		mRenderer, 255, 255, 255, 255
	);
	//è„ïîï«ÇÃï`âÊ
	SDL_Rect wall{
		0, 0, window_width, tickness
	};
	SDL_RenderFillRect(mRenderer, &wall);
	//ï«â∫ïîÇÃï`âÊ
	wall.y = window_height - tickness;
	SDL_RenderFillRect(mRenderer, &wall);
	//ï«âEïîÇÃï`âÊ
	//wall.y = 0;
	//wall.h = window_height;
	//wall.w = tickness;
	//wall.x = window_width - tickness;
	//SDL_RenderFillRect(mRenderer, &wall);
	//paddleÇÃï`âÊ
	/*SDL_Rect paddle{
		tickness, (window_height - paddleH) / 2, tickness, paddleH
	};*/
	SDL_Rect paddle{
		mPaddlePos.x, mPaddlePos.y - paddleH/2, tickness, paddleH
	};
	SDL_Rect paddle2{
		mPaddlePos2.x, mPaddlePos2.y - paddleH / 2, tickness, paddleH
	};
	SDL_RenderFillRect(mRenderer, &paddle);
	SDL_RenderFillRect(mRenderer, &paddle2);

	//ballÇÃï`âÊ
	for (Ball b : balls) {
		SDL_Rect ball{
		static_cast<int>(b.pos.x - tickness / 2),
		static_cast<int>(b.pos.y - tickness / 2),
		tickness, tickness
		};
		SDL_RenderFillRect(mRenderer, &ball);
	}
	
	SDL_RenderPresent(mRenderer);
}