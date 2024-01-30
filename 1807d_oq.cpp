/**
 * @file 1807d_oq.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 1807D - Odd Queries(https://codeforces.com/problemset/problem/1807/D)
 * @version 0.1
 * @date 2024-01-30
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
	int n, q, l, r, k, i;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> q;
		a.resize(n + 1);
		cin >> a[0];
		a[0] %= 2;
		for (i = 1; i < n; i++)
		{
			cin >> a[i];
			a[i] += a[i - 1];
			a[i] %= 2;
		}
		while (q--)
		{
			cin >> l >> r >> k;
			l--, r--;
			if (l == 0)
				(abs(a[n - 1] - a[r]) + (k * (r - l + 1))) % 2 ? cout << "YES\n" : cout << "NO\n";
			else
				(abs(a[n - 1] - a[r]) + a[l - 1] + (k * (r - l + 1))) % 2 ? cout << "YES\n" : cout << "NO\n";
		}
	}
	return (EXIT_SUCCESS);
}
