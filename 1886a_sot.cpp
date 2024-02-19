/**
 * @file 1886a_sot.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Sum of Three(https://codeforces.com/problemset/problem/1886/A)
 * @version 0.1
 * @date 2024-02-19
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
	int n, a, b;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a = 1;
		if (!(n % 3))
			b = 4;
		else
			b = 2;
		if (!((n - b - a) % 3) || n - b - a < 4 || (a == n - b - a) || (b == n - b - a))
			cout << "NO\n";
		else
			cout << "YES\n"
				 << a << ' ' << b << ' ' << n - b - a << '\n';
	}
	return (EXIT_SUCCESS);
}