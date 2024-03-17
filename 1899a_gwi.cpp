/**
 * @file 1899a_gwi.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Game with Integers(https://codeforces.com/problemset/problem/1899/A)
 * @version 0.1
 * @date 2024-03-17
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

	cin >> t;
	while (t--)
	{
		cin >> n;
		cout << (n % 3 ? "First" : "Second") << '\n';
	}
	return (EXIT_SUCCESS);
}
