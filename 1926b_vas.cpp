/**
 * @file 1926b_vas.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vlad and Shapes(https://codeforces.com/contest/1926/problem/B)
 * @version 0.1
 * @date 2024-03-17
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief Function to check if the grid is a square
 *
 * @param grid
 * @return true
 * @return false
 */
bool is_square(vector<string> &grid)
{
	short i = 0, y, x, x1;

	while (grid[i].find('1') == string::npos)
		i++;
	if (i == grid.size())
		return false;
	y = i;
	x = grid[i].find('1');
	x1 = grid[i].find_last_of('1');
	while (i < grid.size() && grid[i].find('1') != string::npos)
	{
		if (grid[i].find('1') != x || grid[i].find_last_of('1') != x1)
			return false;
		if (grid[i].substr(x, x1 - x + 1).find('0') != string::npos)
			return false;
		i++;
	}
	return true;
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n;
	vector<string> grid;

	cin >> t;
	while (t--)
	{
		cin >> n;
		grid.resize(n);
		for (string &row : grid)
			cin >> row;
		is_square(grid) ? cout << "SQUARE\n" : cout << "TRIANGLE\n";
	}
	return (EXIT_SUCCESS);
}