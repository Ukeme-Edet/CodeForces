/**
 * @file 1857a_ac.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Array Coloring(https://codeforces.com/problemset/problem/1857/A)
 * @version 0.1
 * @date 2024-06-08
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
	short t, n, i, a[50];

	cin >> t;
	while (t--)
	{
		cin >> n;
		for (i = 0; i < n; i++)
			cin >> a[i];
		reduce(a, a + n) % 2 ? cout << "NO\n" : cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
