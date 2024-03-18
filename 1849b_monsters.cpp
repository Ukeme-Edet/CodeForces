/**
 * @file 1849b_monsters.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem
 * Monsters(https://codeforces.com/problemset/problem/1849/B)
 * @version 0.1
 * @date 2024-03-18
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
	short t;
	int n, k, i;
	vector<pair<int, int>> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		i = 0;
		for (pair<int, int> &ai : a)
		{
			cin >> ai.first;
			ai.first %= k;
			ai.second = ++i;
		}
		sort(a.begin(), a.end(), [](pair<int, int> &x, pair<int, int> &y){
			return x.first < y.first || (x.first == y.first && x.second < y.second);
		});
		i = 0;
		for (pair<int, int> &ai : a)
		{
			if (ai.first != 0)
				break;
			cout << ai.second << ' ';
			i++;
		}
		sort(a.begin() + i, a.end(), [](pair<int, int> &x, pair<int, int> &y){
			return x.first > y.first || (x.first == y.first && x.second < y.second);
		});
		for (pair<int, int> &ai : a)
		{
			if (ai.first == 0)
				continue;
			cout << ai.second << ' ';
		}
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
