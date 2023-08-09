#include "Game.h"

Game::Game()
{
	int j = 5;
	field.resize(9);
	for (int i = 0; i < 5; i++)
	{
		field[i].resize(j);
		j++;
	}
	j-=2;
	for (int i = 5; i < 9; i++)
	{
		field[i].resize(j);
		j--;
	}
	size = 5;
	field[0][0] = 1;
	field[0][size - 1] = 2;
	field[size +size - 2][0] = 1;
	field[size +size - 2][size - 1] = 2;
	field[size-1][0] = 2;
	field[size -1][size+size - 2] = 1;
	bot = 3;
	player = 3;
}

Game::Game(int newsize)
{
	size = newsize;
	int j = size;
	field.resize(size+size - 1);
	for (int i = 0; i < size; i++)
	{
		field[i].resize(j);
		j++;
	}
	j-=2;
	for (int i = size; i < size + size - 1; i++)
	{
		field[i].resize(j);
		j--;
	}
	field[0][0] = 1;
	field[0][size - 1] = 2;
	field[size + size - 2][0] = 1;
	field[size + size - 2][size - 1] = 2;
	field[size - 1][0] = 2;
	field[size - 1][size + size - 2] = 1;
	bot = 3;
	player = 3;
}


void Game::show()
{
	cout << "   ";
	int c = size - 1;
	cout << "\n";
	for (int i = 0; i < size+size-1; i++)
	{
		//cout << " " << i << " ";
		if (i < size - 1)
		{
			for (int d = 0; d < c * 4; d++)
			{
				cout << " ";
			}
			c--;
			for (int z = 0; z < i; z++)
				cout << "  ";
		}
		if (i > size - 2)
		{
			for (int z = 0; z < i; z++)
				cout << "  ";
		}
		for (int j = 0; j < field[i].size(); j++)
		{
			cout << "[" << field[i][j] << "]" << " ";
		}
		cout << "\n";
	}
}

int Game::check(int x, int y, int play)
{
	if (x > -1 && y > -1 && x < size + size - 1 && y < field[x].size() && field[x][y] == 0)
	{
		if (x < size + size - 2 && y < field[x + 1].size())
		{
			if (field[x + 1][y] == play)
			{
				return 0;
			}
		}
		if (y < field[x].size() - 1)
		{
			if (field[x][y + 1] == play)
			{
				return 0;
			}

		}
		if (x < size + size - 2 && x >= 4 && y <= field[x+1].size() && y > 0)
		{
			if (field[x + 1][y - 1] == play)
			{
				return 0;
			}

		}

		if (x < size + size - 2 && x < 4 && y < field[x + 1].size() - 1 )
		{
			if (field[x + 1][y + 1] == play)
			{
				return 0;
			}

		}

		if (x > 0 && y < field[x - 1].size())
		{
			if (field[x - 1][y] == play)
			{
				return 0;
			}

		}
		if (x > 0 && y < field[x - 1].size() - 1 && x > 4)
		{
			if (field[x - 1][y + 1] == play)
			{
				return 0;
			}

		}
		if (x > 0 && y <= field[x - 1].size() && x<=4 && y > 0)
		{
			if (field[x - 1][y - 1] == play)
			{
				return 0;
			}

		}
		if (y > 0 && y < field[x].size())
		{
			if (field[x][y - 1] == play)
			{
				return 0;
			}

		}
	}	
	return 1;
}


int Game::place(int x, int y, int you , int enemy, int key)
{
	if (check(x,y,you) == 0)
	{
		field[x][y] = you;
		if (you == 1)
			player += 1;
		else
			bot += 1;
		if (x < size + size - 2 && y < field[x + 1].size())
		{
			if (field[x + 1][y] == enemy)
			{ 
				field[x + 1][y] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}
		}
		if (y < field[x].size() - 1)
		{
			if (field[x][y + 1] == enemy)
			{ 
				field[x][y + 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}
				
		}
		if (x < size + size - 2 && x >= 4 && y <= field[x + 1].size() && y > 0)
		{
			if (field[x + 1][y - 1] == enemy)
			{
				field[x + 1][y - 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}
				
		}

		if (x < size + size - 2 && x < 4 && y < field[x + 1].size() - 1)
		{
			if (field[x + 1][y + 1] == enemy)
			{
				field[x + 1][y + 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}

		}

		if (x > 0 && y < field[x - 1].size())
		{
			if (field[x - 1][y] == enemy)
			{
				field[x - 1][y] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}
				
		}
		if (y > 0 && y < field[x].size())
		{
			if (field[x][y - 1] == enemy)
			{
				field[x][y - 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}

		}
		if (x > 0 && y < field[x - 1].size() - 1 && x > 4)
		{
			if (field[x - 1][y + 1] == enemy)
			{
				field[x - 1][y + 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}

		}
		if (x > 0 && y <= field[x - 1].size() && x <= 4 && y > 0)
		{
			if (field[x - 1][y - 1] == enemy)
			{
				field[x - 1][y - 1] = you;
				if (you == 1)
				{
					player += 1;
					bot -= 1;
				}
				else
				{
					player -= 1;
					bot += 1;
				}
			}

		}
		if (you == 1)
			return player;
		else 
			return bot;
	}
	else
	{
	if (key == 1)
		cout << "Enter coordinate : ";
		return -100;
	}
}




void Game::Botturn(Game& a , int deapth,int you,int enemy)
{
	pair<pair<int, int>, int> move = make_pair(make_pair(0, 0), 0);
	if(deapth > 0)
	move = minmax(a, deapth, 1,you,enemy);
	else 
	{
		pair<int, int> temp;
		int k = 0, p = player, b = bot;
		pair<pair<int, int>, int> res;
		vector<vector<int>> save = field;
		vector<pair<pair<int, int>, int>> moves;
		for (int i = 0; i < size + size - 1; i++)
		{
			for (int j = 0; j < field[i].size(); j++)
			{
				k = place(i, j,you,enemy,2);
				if (k != -100)
				{
					temp.first = i;
					temp.second = j;
					move.first = temp;
					move.second = k;
					moves.push_back(move);
				}
				player = p;
				bot = b;
				field = save;
			}
		}
		if (moves.size() > 0)
		{
			srand( time(0));
			k = rand() % moves.size();
			move = moves[k];
		}
	}
	place(move.first.first, move.first.second,you,enemy,2);
}

pair<pair<int, int>, int> Game::minmax(Game a, int deapth , int turn,int you,int enemy)
{
	vector<pair<pair<int, int>, int>> moves;
	int k = 0,p = player,b = bot, max = -100, min = 100;
	pair<pair<int, int>, int> move;
	pair<int, int> temp;
	vector<int> d;
	pair<pair<int, int>, int> res = make_pair(make_pair(0, 0), 0);
	vector<vector<int>> time = field;
	if (turn == 1)
	{
		for (int i = 0; i < size + size - 1; i++)
		{
			for (int j = 0; j < field[i].size(); j++)
			{
				k = place(i, j,you,enemy,2);
				if (k != -100)
				{
					temp.first = i;
					temp.second = j;
					move.first = temp;
					move.second = k;
					if (deapth > 1)
					{
						res = minmax(a, deapth - 1, 0,enemy,you);
					}
					if (res.second != 0)
					{
						move.second = res.second;
					}
					moves.push_back(move);
					
				}
				player = p;
				bot = b;
				field = time;
			}
		}
		for (int f = 0; f < moves.size(); f++)
		{
			if (moves[f].second < min)
			{
				res.first = moves[f].first;
				res.second = moves[f].second;
				min = moves[f].second;
			}
		}
	}
	else
	{
		for (int i = 0; i < size + size - 1; i++)
		{
			for (int j = 0; j < field[i].size(); j++)
			{
				k = place(i, j,you,enemy,2);
				if (k != -100)
				{
					temp.first = i;
					temp.second = j;
					move.first = temp;
					move.second = k;
					if (deapth > 1)
					{
						res = minmax(a, deapth - 1, 1,enemy,you);
					}
					if (res.second != 0)
					{
						move.second = res.second;
					}
					moves.push_back(move);
				}
				player = p;
				bot = b;
				field = time;
			}
		}
		for (int f = 0; f < moves.size(); f++)
		{
			if (moves[f].second > max)
			{
				res.first = moves[f].first;
				res.second = moves[f].second;
				max = moves[f].second;
			}
		}
	}
	return res;
}

int Game::winner(int key)
{
	if (key == 1)
	{
		if (player + bot == 61)
		{
			if (player > bot)
			{
				cout << "Player win with score : " << player;
			}
			if (player < bot)
			{
				cout << "Computer win with score : " << bot;
			}
			if (player == bot) cout << "drawn game";
			return 0;
		}
		return 1;
	}
	else
	{
		if (player + bot == 61)
		{
			if (player > bot)
			{
				cout << "Computer#1 win with score : " << player;
			}
			if (player < bot)
			{
				cout << "Computer#2 win with score : " << bot;
			}
			if (player == bot) cout << "drawn game";
			return 0;
		}
		return 1;
	}
}
