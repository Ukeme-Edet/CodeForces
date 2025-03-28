/**
 * @file 1896a_js.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Jagged Swaps(https://codeforces.com/problemset/problem/1896/A)
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
	short t, n;
	vector<short> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (short &ai : a)
			cin >> ai;
		a[0] == 1 ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
