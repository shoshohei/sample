#pragma once
#include "SDL/SDL.h"
#include <string>
#include <vector>
#include <unordered_map>
#include "Math.h"

class Game {
public:
	Game();
	bool Initialize();
	void RunLoop();
	void Shutdown();

	void AddActor(class Actor* actor);
	void RemoveActor(class Actor* actor);
	void AddSprite(class SpriteComponent* sprite);
	void RemoveSprite(class SpriteComponent* sprite);

	SDL_Texture* GetTexture(const std::string& filename);
	
	class Grid* GetGrid() { return mGrid; }
	std::vector<class Enemy*>& GetEnemies() { return mEnemies; };
	class Enemy* GetNearestEnemy(const Vector2& pos);
private:
	void ProcessInput();
	void UpdateGame();
	void GenerateOutput();
	void LoadData();
	void UnLoadData();

	std::unordered_map <std::string, SDL_Texture*> mTextures;
	std::vector<class Actor*> mActors;
	std::vector<class Actor*> mPendingActors;
	std::vector<class SpriteComponent*> mSprites;

	SDL_Window* mWindow;
	SDL_Renderer* mRenderer;
	Uint32 mTicksConunt;
	bool mIsRunning;
	bool mUpdatingActors;

	int mWindowHeight;
	int mWindowWidth;

	std::vector<class Enemy*> mEnemies;
	class Grid* mGrid;
	float mNextEnemy;
};