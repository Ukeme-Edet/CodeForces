/**
 * @file 1944a_db.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem  Destroying Bridges(https://codeforces.com/contest/1944/problem/A)
 * @version 0.1
 * @date 2024-03-16
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

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		k >= n - 1 ? cout << "1\n" : cout << n << '\n';
	}
	return (EXIT_SUCCESS);
}
