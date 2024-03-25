/**
 * @file 1873c_tp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Target Practice(https://codeforces.com/contest/1873/problem/C)
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, i, j, x, y, score;
	vector<string> grid(10);

	cin >> t;
	while (t--)
	{
		for (string &row : grid)
			cin >> row;
		score = 0;
		for (i = 0; i < 10; i++)
		{
			for (j = 0; j < 10; j++)
			{
				if (grid[i][j] == 'X')
				{
					x = i, y = j;
					x > 4 ? x = 9 - x : x;
					y > 4 ? y = 9 - y : y;
					score += min(x, y) + 1;
				}
			}
		}
		cout << score << '\n';
	}
	return (EXIT_SUCCESS);
}
