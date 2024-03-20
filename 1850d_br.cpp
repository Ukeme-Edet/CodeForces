/**
 * @file 1850d_br.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Balanced Round(https://codeforces.com/contest/1850/problem/D)
 * @version 0.1
 * @date 2024-03-20
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
	int n, k, ml, i, l;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		sort(a.begin(), a.end());
		l = ml = 1;
		for (i = 1; i < n; i++)
		{
			if (a[i] - a[i - 1] > k)
			{
				ml = max(ml, l);
				l = 1;
			}
			else
				l++;
		}
		ml = max(ml, l);
		cout << n - ml << '\n';
	}
	return (EXIT_SUCCESS);
}
