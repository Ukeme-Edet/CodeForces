/**
 * @file 1941b_pa121.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Rudolf and 121(https://codeforces.com/contest/1941/problem/B)
 * @version 0.1
 * @date 2024-04-10
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
	int n, i;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		for (i = 1; i < n - 1; i++)
		{
			if (a[i - 1] < 0)
				break;
			a[i] -= a[i - 1] * 2, a[i + 1] -= a[i - 1];
			a[i - 1] = 0;
		}
		for (int ai : a)
			if (ai != 0)
			{
				cout << "NO\n";
				goto next;
			}
		cout << "YES\n";
	next:;
	}
	return (EXIT_SUCCESS);
}
