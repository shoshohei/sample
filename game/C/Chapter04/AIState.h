#pragma once
#include "AIComponent.h"

class AIState {
public:
	AIState(class AIComponent* owner)
		:mOwner(owner)
	{ }
	virtual void Update(float deltaTime) = 0;
	virtual void OnEnter() = 0;
	virtual void OnExit() = 0;
	virtual const char* GetName() const = 0;

protected:
	class AIComponent* mOwner;
};

class AIPatrol: public AIState {
public:
	AIPatrol(class AIComponent* owner)
		:AIState(owner)
	{ }

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;
	const char* GetName()const override { return "Patrol"; };
};

class AIAttack : public AIState
{
public:
	AIAttack(class AIComponent* owner)
		:AIState(owner)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Attack";
	}
};

class AISerch : public AIState
{
public:
	AISerch(class AIComponent* owner, class Tower* tower)
		:AIState(owner)
		,mTower(tower)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Serch";
	}
private:
	class Tower* mTower;
};

class AIPaused : public AIState
{
public:
	AIPaused(class AIComponent* owner, class Tower* tower)
		:AIState(owner)
		, mTower(tower)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Serch";
	}
private:
	class Tower* mTower;
};

class AILookOn : public AIState
{
public:
	AILookOn(class AIComponent* owner, class Tower* tower)
		:AIState(owner)
		, mTower(tower)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "LookOn";
	}
private:
	class Tower* mTower;
};

class AIFire : public AIState
{
public:
	AIFire(class AIComponent* owner, class Tower* tower)
		:AIState(owner)
		, mTower(tower)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Fire";
	}
private:
	class Tower* mTower;
};

class AIMove : public AIState
{
public:
	AIMove(class AIComponent* owner)
		:AIState(owner)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Move";
	}
};

class AIDeath : public AIState
{
public:
	AIDeath(class AIComponent* owner)
		:AIState(owner)
	{
	}

	void Update(float deltaTime) override;
	void OnEnter() override;
	void OnExit() override;

	const char* GetName() const override
	{
		return "Death";
	}
};
