#include <stdio.h>
#include <iostream>

using namespace std;

char stage_txt[] = "\
########\n\
# .. p #\n\
# oo   #\n\
#      #\n\
########";

int width_x = 0;
int p_x = 0;
int p_y = 0;
int clear_count = 0;

int stage_re(int x, int y) {
	char c;
	cin >> c;
	if (c == 's') {
		if (stage_txt[(y+1) * width_x + x]==' ') {
			stage_txt[(y + 1) * width_x + x] = 'p';
			p_y++;
			stage_txt[y * width_x + x] = ' ';
		}
		else if (stage_txt[(y + 1) * width_x + x] == 'o') {
			if (stage_txt[(y + 2) * width_x + x] == '.') {
				clear_count++;
				stage_txt[(y + 2) * width_x + x] = '+';
				stage_txt[(y + 1) * width_x + x] = 'p';
				p_y++;
				
				stage_txt[y * width_x + x] = ' ';
			}
			else if (stage_txt[(y + 2) * width_x + x] == ' ') {
				stage_txt[(y + 2) * width_x + x] = 'o';
				stage_txt[(y + 1) * width_x + x] = 'p';
				stage_txt[y * width_x + x] = ' ';
				p_y++;
			}
		}
	}
	else if (c == 'w') {
		if (stage_txt[(y - 1) * width_x + x] == ' ') {
			stage_txt[(y - 1) * width_x + x] = 'p';
			stage_txt[y * width_x + x] = ' ';
			p_y--;
		}
		else if (stage_txt[(y - 1) * width_x + x] == 'o') {
			//cout << "in_o";
			if (stage_txt[(y - 2) * width_x + x] == '.') {
				//cout << "in_." << x << y << "\n";
				clear_count++;
				stage_txt[(y - 2) * width_x + x] = '+';
				stage_txt[(y - 1) * width_x + x] = 'p';
				stage_txt[y * width_x + x] = ' ';

				p_y--;
			}
			else if (stage_txt[(y-2) * width_x + x] == ' ') {
				stage_txt[(y-2) * width_x + x] = 'o';
				stage_txt[(y-1) * width_x + x] = 'p';
				stage_txt[y * width_x + x] = ' ';
				p_y--;
			}
		}
	}
	else if (c == 'a') {
		if (stage_txt[y * width_x + x-1] == ' ') {
			stage_txt[y * width_x + x-1] = 'p';
			stage_txt[y * width_x + x] = ' ';
			p_x--;
		}
		else if (stage_txt[y * width_x + x-1] == 'o') {
			if (stage_txt[y * width_x + x-2] == '.') {
				cout << "in\n";
				clear_count++;
				stage_txt[y * width_x + x-2] = '+';
				stage_txt[y * width_x + x-1] = 'p';
				p_x--;
				stage_txt[y * width_x + x] = ' ';
			}
			else if (stage_txt[y * width_x+x - 2] == ' ') {
				stage_txt[y * width_x + x - 2] = 'o';
				stage_txt[y * width_x + x - 1] = 'p';
				stage_txt[y * width_x + x] = ' ';
				p_x--;
			}
		}
	}
	else if (c == 'd') {
		if (stage_txt[y * width_x + x+1] == ' ') {
			stage_txt[y * width_x + x+1] = 'p';
			stage_txt[y * width_x + x] = ' ';
			p_x++;
		}
		else if (stage_txt[y * width_x + x+1] == 'o') {
			if (stage_txt[y * width_x + x+2] == '.') {
				clear_count++;
				stage_txt[y * width_x + x+2] = '+';
				stage_txt[y * width_x + x+1] = 'p';
				p_x++;
				stage_txt[y * width_x + x] = ' ';
			}
			else if (stage_txt[y * width_x + x + 2] == ' ') {
				stage_txt[y * width_x + x + 2] = 'o';
				stage_txt[y * width_x + x + 1] = 'p';
				stage_txt[y * width_x + x] = ' ';
				p_x++;
			}
		}
	}
	cout << stage_txt << "\n";
	return 0;
}

int main(void) {
	//cout << sizeof(stage_txt);
	
	for (int i = 0; i < sizeof(stage_txt);i++) {
		if (stage_txt[i] == '\n') {
			width_x = i + 1;
			break;
		}
	}
	for (int i = 0;i < sizeof(stage_txt);i++) {
		//cout << i << stage_txt[i] << "\n";
		if (stage_txt[i] == 'p') {
			p_x = i % width_x;
			p_y = int(i/width_x);
		}
	}
	cout << p_x << "\t" << p_y << "\t" << width_x << "\n";
	cout << stage_txt << "\n";
	while (clear_count != 2) {
		//cout << "in" << "\n";
		stage_re(p_x, p_y);
		//cout << p_x << p_y << "\n";
	}
	cout << "CLEAR!" << "\n";
}