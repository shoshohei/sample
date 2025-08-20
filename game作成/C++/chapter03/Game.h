#pragma once
#include "SDL/SDL.h"
#include <unordered_map>
#include <vector>
#include <string>

class Game {
public:
	Game();
	bool Initialize();
	void RunLoop();
	void Shutdown();

	SDL_Texture* Game::GetTexture(const std::string& fileName);

	void AddActor(class Actor* actor);
	void RemoveActor(class Actor* actor);
	void AddSprite(class SpriteComponent* sprite);
	void RemoveSprite(class SpriteComponent* sprite);
	void AddAsteroid(class Asteroid* actor);
	void RemoveAsteroid(class Asteroid* actor);

	std::vector<class Asteroid*>& GetAsteroids() { return mAsteroids; };

	int GetWindowHeight()const { return mWindowsHeight; };
	int GetWindowsWidth()const { return mWindowsWidth; };

private:
	void ProcessInput();
	void UpdateGame();
	void GenerateOutput();
	void LoadData();
	void UnloadData();
	
	std::unordered_map<std::string, SDL_Texture*> mTextures;
	std::vector<class SpriteComponent*> mSprites;

	std::vector<class Actor*> mActors;
	std::vector<class Actor*> mPendingActors;
	std::vector<class Asteroid*> mAsteroids;

	SDL_Window* mWindow;
	SDL_Renderer* mRenderer;
	Uint32 mTickCount;
	bool mIsRunning;
	bool mUpdatingActors;

	const int mWindowsWidth = 1024;
	const int mWindowsHeight = 768;

protected:

	class Ship* mShip;
};