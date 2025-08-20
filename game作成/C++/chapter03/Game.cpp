#include "Game.h"
#include "Actor.h"
#include "SDL/SDL_image.h"
#include <vector>
#include "SpriteComponent.h"
#include <algorithm>
#include "Asteroid.h"
#include "Ship.h"




Game::Game()
	:mWindow(nullptr)
	, mRenderer(nullptr)
	, mIsRunning(true)
	, mUpdatingActors(false)
	, mShip(nullptr)
{

}

bool Game::Initialize() {
	if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO) != 0) {
		return false;
	}

	mWindow = SDL_CreateWindow("chapter3", 100, 100, mWindowsWidth, mWindowsHeight, 0);
	if (!mWindow) {
		return false;
	}

	mRenderer = SDL_CreateRenderer(mWindow, -1, SDL_RENDERER_ACCELERATED|SDL_RENDERER_PRESENTVSYNC);
	if (!mRenderer) {
		return false;
	}

	if (IMG_Init(IMG_INIT_PNG) == 0) {
		return false;
	}
	LoadData();
	mTickCount = SDL_GetTicks();

	return true;
}

void Game::LoadData() {
	mShip = new Ship(this);
	mShip->SetPosition(Vector2(mWindowsWidth/2.0, mWindowsHeight/2.0f));
	mShip->SetRotation(Math::PiOver2);

	const int numAsteroid = 20;
	for (int i = 0;i < numAsteroid;i++) {
		new Asteroid(this);
	}
}

void Game::UnloadData()
{
	// Delete actors
	// Because ~Actor calls RemoveActor, have to use a different style loop
	while (!mActors.empty())
	{
		delete mActors.back();
	}

	// Destroy textures
	for (auto i : mTextures)
	{
		SDL_DestroyTexture(i.second);
	}
	mTextures.clear();
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

void Game::ProcessInput() {
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type) {
		case SDL_QUIT:
			mIsRunning = false;
			break;
		}
	}

	const Uint8* state = SDL_GetKeyboardState(NULL);
	if (state[SDL_SCANCODE_ESCAPE]) {
		mIsRunning = false;
	}

	mUpdatingActors = true;
	for (auto actor : mActors) {
		actor->ProcessInput(state);
	}
	mUpdatingActors = false;
}

void Game::UpdateGame() {
	//printf("%d\n", mActors.size());
	while (!SDL_TICKS_PASSED(SDL_GetTicks(), mTickCount + 16));

	float deltaTime = (SDL_GetTicks() - mTickCount) / 1000.0f;
	if (deltaTime > 0.05f) {
		deltaTime = 0.05f;
	}
	mTickCount = SDL_GetTicks();

	mUpdatingActors = true;
	for (auto actor : mActors) {
		actor->Update(deltaTime);
	}
	mUpdatingActors = false;
	
	for (auto actor : mPendingActors) {
		mActors.emplace_back(actor);
	}
	mPendingActors.clear();

	std::vector<class Actor*> deadActors;
	for (auto actor : mActors) {
		if (actor->GetState() == Actor::EDEAD) {
			deadActors.emplace_back(actor);
		}
	}
	for (auto actor : deadActors) {
		delete actor;
	}
}

void Game::GenerateOutput() {
	SDL_SetRenderDrawColor(mRenderer, 32, 160, 128, 0);
	SDL_RenderClear(mRenderer);
	for (auto sprite : mSprites) {
		sprite->Draw(mRenderer);
	}
	SDL_RenderPresent(mRenderer);
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
		std::iter_swap(iter, mPendingActors.end() - 1);
		mPendingActors.pop_back();
	}

	iter = std::find(mActors.begin(), mActors.end(), actor);
	if (iter != mActors.end()) {
		std::iter_swap(iter, mActors.end() - 1);
		mActors.pop_back();
	}
}

void Game::AddSprite(SpriteComponent* sprite) {
	int myDrawOrder = sprite->GetDrawOrder();
	auto iter = mSprites.begin();
	for (;iter != mSprites.end();++iter) {
		if (myDrawOrder < (*iter)->GetDrawOrder()) {
			break;
		}
	}
	mSprites.insert(iter, sprite);
}

void Game::RemoveSprite(SpriteComponent* sprite) {
	auto iter = std::find(mSprites.begin(), mSprites.end(), sprite);
	mSprites.erase(iter);
}

void Game::AddAsteroid(Asteroid* actor) {
	mAsteroids.emplace_back(actor);
}

void Game::RemoveAsteroid(Asteroid* actor) {
	auto iter = std::find(mAsteroids.begin(), mAsteroids.end(), actor);
	if (iter != mAsteroids.end()) {
		mAsteroids.erase(iter);
	}
}

SDL_Texture* Game::GetTexture(const std::string& fileName)
{
	SDL_Texture* tex = nullptr;
	// Is the texture already in the map?
	auto iter = mTextures.find(fileName);
	if (iter != mTextures.end())
	{
		tex = iter->second;
	}
	else
	{
		// Load from file
		SDL_Surface* surf = IMG_Load(fileName.c_str());
		if (!surf)
		{
			SDL_Log("Failed to load texture file %s", fileName.c_str());
			return nullptr;
		}

		// Create texture from surface
		tex = SDL_CreateTextureFromSurface(mRenderer, surf);
		SDL_FreeSurface(surf);
		if (!tex)
		{
			SDL_Log("Failed to convert surface to texture for %s", fileName.c_str());
			return nullptr;
		}

		mTextures.emplace(fileName.c_str(), tex);
	}
	return tex;
}
