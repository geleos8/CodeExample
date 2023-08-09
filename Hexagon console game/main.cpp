#include "Game.h"

int main()
{
	int x = 0, y = 0, key,depth,depth2;
	
	Game Hexagon;
	cout << "Enter 1 - play player vs computer or enter 2 - play computer vs computer : ";
	cin >> key;

	if (key == 1)
	{
		cout << "Enter depth of calculating (recommended 0 or 2 or 4 or deapth < 5) ";
		cin >> depth;
		Hexagon.show();
		cout << "When your turn  enter coordinate x and y (): ";
		while (Hexagon.winner(key))
		{
			while (Hexagon.place(x, y, 1, 2,key) == -100)
			{
				cin >> y >> x;
			}
			Hexagon.show();
			Hexagon.Botturn(Hexagon, depth, 2, 1);
			Hexagon.show();
		}
	}
	else if (key == 2)
	{
		cout << "Enter depth of calculating for computer#1 (recommended 0 or 2 or 4 or deapth < 5) ";
		cin >> depth;
		cout << "Enter depth of calculating for computer#2 (recommended 0 or 2 or 4 or deapth < 5) ";
		cin >> depth2;
		while (Hexagon.winner(key))
		{
			Hexagon.Botturn(Hexagon, depth, 1, 2);
			Hexagon.show();
			if (Hexagon.winner(key) == 0)
				break;
			Hexagon.Botturn(Hexagon, depth2, 2, 1);
			Hexagon.show();
		}
	}
	else
		cout << "Wrong key. Restart the game.";
}

