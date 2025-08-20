#include "GameLib/Framework.h"
using namespace GameLib;
#include <fstream>
using namespace std;
enum Object {
	OBJ_SPACE,
	OBJ_PLAYER,
	OBJ_PLAYER_ON_TARGET,
	OBJ_BOX,
	OBJ_BOX_ON_TARGET,
	OBJ_WALL,
	OBJ_TARGET,
	OBJ_UNKNOWN
};

void readFile(char** stage, int* len, const char* name);
void Initialize(Object* state, char* stageData, int width);
bool isClear(Object* state, int height, int width);
void Update(Object* state, char c, int height, int width);
void drawStage(Object* state, int height, int width);
void main_loop();

namespace GameLib {
	void Framework::update() {
		//unsigned* vram = videoMemory();
		////int width = width();
		//int width = 10;
		//cout << "!!!" << width << endl;
		//for (int i = 100;i < 200;i++)
		//	for (int j = 100;j < 200;j++)
		//		vram[i * width + j] = 0xf0f0f0;
		main_loop();
	}
}

void main_loop() {
	const char* file_name = "stage_txt.txt";

	char* stage;
	int fileSize;
	readFile(&stage, &fileSize, file_name);
	//cout << fileSize;
	//cout << stage << endl;
	int width = 0;
	int height = 0;
	int x = 0;
	int y = 1;
	int index_p = 0;
	for (int i = 0;i < fileSize;i++) {
		switch (stage[i]) {
		case ' ': case '.': case 'o': case '#':
			x++;
			break;
		case '\n':
			y++;
			height = max(height, y);
			width = max(width, x);
			x = 0;
			break;
		}
	}
	Object* state = new Object[width * height];
	Initialize(state, stage, width);
	//cout << isClear(state, height, width) << endl;
	while (1) {

		drawStage(state, height, width);
		if (isClear(state, height, width)) {
			break;
		}
		char c;
		cin >> c;
		Update(state, c, height, width);
	}
	cout << "CLEAR!!!!" << endl;

}


void readFile(char** stage, int* len, const char* name) {
	ifstream in(name);
	if (!in) {
		*stage = 0;
		*len = 0;
	}
	else {
		in.seekg(0, ifstream::end);
		*len = static_cast<int>(in.tellg());
		//cout << *len << endl;
		in.seekg(0, ifstream::beg);
		*stage = new char[*len];
		in.read(*stage, *len);
	}
}

void Initialize(Object* state, char* stageData, int width) {
	const char* d = stageData;
	int x = 0;
	int y = 0;
	while (*d != '\0') {
		Object t;
		switch (*d) {
		case '#': t = OBJ_WALL;break;
		case ' ': t = OBJ_SPACE;break;
		case 'o': t = OBJ_BOX;break;
		case 'p': t = OBJ_PLAYER;break;
		case '.': t = OBJ_TARGET;break;
		case '\n':
			t = OBJ_UNKNOWN;
			x = 0;
			y++;
			break;
		default: t = OBJ_UNKNOWN;break;
		}
		d++;
		if (t != OBJ_UNKNOWN) {
			state[y * width + x] = t;
			x++;
		}
	}
}

void drawStage(Object* state, int height, int width) {
	const char out_char[] = { ' ', 'p', 'P', 'o', 'O', '#', '.', '\n' };

	for (int y = 0; y < height; ++y) {
		for (int x = 0; x < width; ++x) {
			Object obj = state[width * y + x];
			cout << out_char[obj];
		}
		cout << endl;
	}

}

void Update(Object* state, char c, int height, int width) {
	int dx = 0;
	int dy = 0;
	switch (c) {
	case 'a': dx = -1;break;
	case 'd': dx = 1;break;
	case 'w': dy = -1;break;
	case 's': dy = 1;break;
	}
	//playerの座標
	int i = 0;
	for (i = 0;i < width * height;i++) {
		if (state[i] == OBJ_PLAYER || state[i] == OBJ_PLAYER_ON_TARGET) {
			break;
		}
	}
	int px = i % width;
	int py = i / width;
	int p = py * width + px;
	//cout << px << '\t' << py << endl;
	//移動先の座標
	int dpx = px + dx;
	int dpy = py + dy;

	//cout << dpx << '\t' << dpy << endl;
	int dp = dpy * width + dpx;
	//移動先が壁か判定
	if (dpx <= 0 || dpx >= width || dpy <= 0 || dpy >= height) {
		return;
	}
	//移動先が箱以外
	if (state[dp] == OBJ_SPACE || state[dp] == OBJ_TARGET) {
		state[dp] = (state[dp] == OBJ_TARGET) ? OBJ_PLAYER_ON_TARGET : OBJ_PLAYER;
		state[p] = (state[p] == OBJ_PLAYER_ON_TARGET) ? OBJ_TARGET : OBJ_SPACE;
	}
	//移動先が箱
	else if (state[dp] == OBJ_BOX || state[dp] == OBJ_BOX_ON_TARGET) {
		int ddpx = dpx + dx;
		int ddpy = dpy + dy;
		int ddp = ddpy * width + ddpx;
		if (state[ddp] == OBJ_BOX || state[ddp] == OBJ_BOX_ON_TARGET) {
			return;
		}
		//cout << ddpx << '\t' << ddpy << endl;
		//壁移動先の座標が壁か判定
		if (ddpx <= 0 || ddpx >= width || ddpy <= 0 || ddpy >= height) {
			return;
		}
		state[ddp] = (state[ddp] == OBJ_TARGET) ? OBJ_BOX_ON_TARGET : OBJ_BOX;
		state[dp] = (state[dp] == OBJ_TARGET || state[dp] == OBJ_BOX_ON_TARGET) ? OBJ_PLAYER_ON_TARGET : OBJ_PLAYER;
		state[p] = (state[p] == OBJ_PLAYER_ON_TARGET) ? OBJ_TARGET : OBJ_SPACE;
	}
}

bool isClear(Object* state, int height, int width) {
	for (int i = 0;i < width * height;i++) {
		if (state[i] == OBJ_BOX) {
			return false;
		}
	}
	return true;
}