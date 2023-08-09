
#include <iostream>
#include <vector>
#include <map>
#include <ctime>
using namespace std;

class Game
{
public:
	Game();
	Game(int newsize);
	void show();
	int place(int x, int y, int you, int enemy, int key);
	void Botturn(Game& a, int deapth, int you, int enemy);
	pair<pair<int, int>, int> minmax(Game a, int deapth, int turn, int you, int enemy);
	int check(int x, int y, int play);
	int winner(int key);

private:
	int size;
	int player;
	int bot;
	vector<vector<int>> field;
};

