#include "GameLib/Framework.h"

namespace GameLib{
	void Framework::update(){
		unsigned* vram = videoMemory();
		for(int i=0;i<3000;i++) vram[i] = 0xff0000;
	}
}
