#include "Game.h"
#include "Actor.h"
#include "SDL/SDL_image.h"
#include <algorithm>
#include "SpriteComponent.h"
#include "Enemy.h"
#include "Grid.h"
#include "AIState.h"
#include "AIComponent.h"


Game::Game()
	:mWindow(nullptr)
	, mRenderer(nullptr)
	, mIsRunning(true)
	, mUpdatingActors(false)
{

}

bool Game::Initialize() {
	if (SDL_Init(SDL_INIT_AUDIO | SDL_INIT_VIDEO) != 0) {
		SDL_Log("SDL Error : %s", SDL_GetError());
		return false;
	}
	mWindow = SDL_CreateWindow("chapter4",100, 200, 1024, 768, 0);
	if (!mWindow) {
		SDL_Log("SDL Error : %s", SDL_GetError());
		return false;
	}
	mRenderer = SDL_CreateRenderer(mWindow, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
	if (!mRenderer) {
		SDL_Log("SDL Error : %s", SDL_GetError());
		return false;
	}
	if (IMG_Init(IMG_INIT_PNG) == 0) {
		SDL_Log("SDL Error : %s", SDL_GetError());
		return false;
	}

	LoadData();
	mTicksCount = SDL_GetTicks();

	return true;
}

void Game::RunLoop() {
	while (mIsRunning) {
		ProcessInput();
		UpdateGame();
		GenerateOutput();
	}
}

void Game::Shutdown() {
	UnloadData();
	IMG_Quit();
	SDL_DestroyRenderer(mRenderer);
	SDL_DestroyWindow(mWindow);
	SDL_Quit();
}

void Game::AddActor(Actor* actor) {
	if (mUpdatingActors) {
		mPendingActors.emplace_back(actor);
	}
	else {
		mActors.emplace_back(actor);
	}
}

void Game::RemoveActor(Actor* actor) {
	auto iter = std::find(mPendingActors.begin(), mPendingActors.end(), actor);
	if (iter != mPendingActors.end()) {
		std::iter_swap(iter, mPendingActors.end()-1);
		mPendingActors.pop_back();
	}

	iter = std::find(mActors.begin(), mActors.end(), actor);
	if (iter != mActors.end()) {
		std::iter_swap(iter, mActors.end()-1);
		mActors.pop_back();
	}
}

void Game::AddSprite(SpriteComponent* sprite) {
	int myDrawOrder = sprite->GetDrawOrder();
	auto iter = mSprites.begin();
	for (;iter != mSprites.end();++iter) {
		if ((*iter)->GetDrawOrder() > myDrawOrder) {
			break;
		}
	}
	mSprites.insert(iter, sprite);
}

void Game::RemoveSprite(SpriteComponent* sprite) {
	auto iter = std::find(mSprites.begin(), mSprites.end(), sprite);
	mSprites.erase(iter);
}

SDL_Texture* Game::GetTexture(const std::string& filename) {
	SDL_Texture* tex = nullptr;
	auto iter = mTextures.find(filename);
	if (iter != mTextures.end()) {
		tex = iter->second;
	}
	else {
		SDL_Surface* suf = IMG_Load(filename.c_str());
		if (!suf) {
			SDL_Log("SDL Error : %s", SDL_GetError());
			return nullptr;
		}
		tex = SDL_CreateTextureFromSurface(mRenderer, suf);
		SDL_FreeSurface(suf);
		if (!tex) {
			SDL_Log("SDL Error : %s", SDL_GetError());
			return nullptr;
		}
		mTextures.emplace(filename.c_str(), tex);
	}
	return tex;
}

void Game::ProcessInput() {
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type)
		{
		case SDL_QUIT:
			mIsRunning = false;
		default:
			break;
		}
	}
	const Uint8* keyState = SDL_GetKeyboardState(NULL);
	if (keyState[SDL_SCANCODE_ESCAPE]) {
		mIsRunning = false;
	}
	if (keyState[SDL_SCANCODE_B]) {
		mGrid->BuildTower();
	}

	int x, y;
	Uint32 buttons = SDL_GetMouseState(&x, &y);
	if (SDL_BUTTON(buttons) & SDL_BUTTON_LEFT) {
		mGrid->ProcessClick(x, y);
	}
	mUpdatingActors = true;
	for (auto actor : mActors)
	{
		actor->ProcessInput(keyState);
	}
	mUpdatingActors = false;
}

void Game::UpdateGame() {
	while (!SDL_TICKS_PASSED(SDL_GetTicks(),  mTicksCount+16));
	float deltaTime = (SDL_GetTicks() - mTicksCount)/1000.0f;
	if (deltaTime > 0.05f) {
		deltaTime = 0.05f;
	}
	mTicksCount = SDL_GetTicks();

	mUpdatingActors = true;
	for (auto actor : mActors) {
		actor->Update(deltaTime);
	}
	mUpdatingActors = false;

	for (auto p : mPendingActors) {
		mActors.emplace_back(p);
	}
	mPendingActors.clear();

	std::vector<Actor*> deadActors;
	for (auto actor : mActors) {
		if (actor->GetState() == Actor::EDead) {
			deadActors.emplace_back(actor);
		}
	}

	for (auto actor : deadActors) {
		delete actor;
	}
}

void Game::GenerateOutput() {
	SDL_SetRenderDrawColor(mRenderer, 128, 0, 16, 0);
	SDL_RenderClear(mRenderer);
	for (auto s : mSprites) {
		s->Draw(mRenderer);
	}
	SDL_RenderPresent(mRenderer);
}

void Game::LoadData() {

	mGrid = new Grid(this);
}

void Game::UnloadData() {
	while (!mActors.empty()) {
		delete mActors.back();
	}
	for (auto t : mTextures) {
		SDL_DestroyTexture(t.second);
	}
	mTextures.clear();
}

Enemy* Game::GetNearestEnemy(const Vector2& pos)
{
	Enemy* best = nullptr;

	if (mEnemies.size() > 0)
	{
		best = mEnemies[0];
		// Save the distance squared of first enemy, and test if others are closer
		float bestDistSq = (pos - mEnemies[0]->GetPosition()).LengthSq();
		for (size_t i = 1; i < mEnemies.size(); i++)
		{
			float newDistSq = (pos - mEnemies[i]->GetPosition()).LengthSq();
			if (newDistSq < bestDistSq)
			{
				bestDistSq = newDistSq;
				best = mEnemies[i];
			}
		}
	}

	return best;
}
