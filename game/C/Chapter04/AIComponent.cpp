#include "AIComponent.h"
#include "Actor.h"
#include "AIState.h"
#include "SDL/SDL_log.h"

AIComponent::AIComponent(Actor* actor)
	:Component(actor)
{

}

void AIComponent::RegisterState(AIState* state) {
	mStateMap.emplace(state->GetName(), state);
}

void AIComponent::Update(float deltaTime) {
	if (mCurrentState) {
		mCurrentState->Update(deltaTime);
	}
}

void AIComponent::ChangeState(const std::string& name) {
	if (mCurrentState) {
		mCurrentState->OnExit();
	}

	auto iter = mStateMap.find(name);
	if (iter != mStateMap.end()) {
		mCurrentState = iter->second;
		mCurrentState->OnEnter();
	}
	else {
		SDL_Log("AIState %s don't exist in StateMap", name.c_str());
		mCurrentState = nullptr;
	}
}

//void AIComponent::Update(float deltaTime) {
//	switch (mState)
//	{
//	case AIComponent::Patrol:
//		UpdatePatrol(deltaTime);
//		break;
//	case AIComponent::Death:
//		UpdateDeah(deltaTime);
//		break;
//	case AIComponent::Attack:
//		UpdateAttack(deltaTime);
//		break;
//	default:
//		break;
//	}
//}
//
//void AIComponent::ChangeState(AIState newState) {
//	switch (mState)
//	{
//	case AIComponent::Patrol:
//		ExitPatrol();
//		break;
//	case AIComponent::Death:
//		ExitDeath();
//		break;
//	case AIComponent::Attack:
//		ExitAttack();
//		break;
//	default:
//		break;
//	}
//
//	mState = newState;
//
//	switch (mState)
//	{
//	case AIComponent::Patrol:
//		EnterPatrol();
//		break;
//	case AIComponent::Death:
//		EnterDeath();
//		break;
//	case AIComponent::Attack:
//		EnterAttack();
//		break;
//	default:
//		break;
//	}
//}