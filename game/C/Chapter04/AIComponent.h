#pragma once
#include "Component.h"
#include <string>
#include <unordered_map>

class AIComponent :public Component {
public:
	/*enum AIState {
		Patrol,
		Death,
		Attack
	};*/
	AIComponent(class Actor* actor);
	void Update(float deltaTime);
	//void ChangeState(AIState newState);
	void ChangeState(const std::string& name);
	void RegisterState(class AIState* state);

private:
	//AIState mState;
	std::unordered_map<std::string, class AIState*> mStateMap;
	class AIState* mCurrentState;
};