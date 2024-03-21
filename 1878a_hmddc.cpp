/**
 * @file 1878a_hmddc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem How Much Does Daytona Cost?(https://codeforces.com/problemset/problem/1878/A)
 * @version 0.1
 * @date 2024-03-21
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
	short t, n, k;
	vector<short> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		for (short &ai : a)
			cin >> ai;
		find(a.begin(), a.end(), k) != a.end() ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
