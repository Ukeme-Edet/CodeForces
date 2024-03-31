/**
 * @file 1722g_eoxor.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Even-Odd XOR(http://codeforces.com/contest/1722/problem/G)
 * @version 0.1
 * @date 2024-03-31
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
	int n, i, c1, c2;
	long long al;

	cin >> t;
	while (t--)
	{
		cin >> n;
		c1 = c2 = 0;
		for (i = 0; i < n - 2; i++)
			c1 ^= i, c2 ^= i + 1;
		al = ((long long)1 << 31) - 1;
		if (c1)
		{
			for (i = 0; i < n - 2; i++)
				cout << i << ' ';
			c1 ^= al;
			cout << al << ' ' << c1 << '\n';
		}
		else
		{
			for (i = 0; i < n - 2; i++)
				cout << i + 1 << ' ';
			c2 ^= al;
			cout << al << ' ' << c2 << '\n';
		}
	}
	return (EXIT_SUCCESS);
}
