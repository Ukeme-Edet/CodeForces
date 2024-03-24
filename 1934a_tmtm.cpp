/**
 * @file 1934a_tmtm.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Too Min Too Max(https://codeforces.com/contest/1934/problem/A)
 * @version 0.1
 * @date 2024-03-24
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
	short t, n, i;
	int ans;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		sort(a.begin(), a.end());
		cout << abs(a[0] - a[n - 2]) + abs(a[n - 2] - a[1]) + abs(a[1] - a[n - 1]) + abs(a[n - 1] - a[0]) << '\n';
	}
	return (EXIT_SUCCESS);
}
