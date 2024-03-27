/**
 * @file 1828b_ps.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Permutation Swap(https://codeforces.com/contest/1828/problem/B)
 * @version 0.1
 * @date 2024-03-26
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
	int n, k, i, pi;
	bool first;

	cin >> t;
	while (t--)
	{
		cin >> n;
		i = first = 1;
		while (n--)
		{
			cin >> pi;
			if (pi != i)
			{
				if (first)
					k = abs(pi - i);
				else
					k = __gcd(k, abs(pi - i));
				first = 0;
			}
			i++;
		}
		cout << k << '\n';
	}
	return (EXIT_SUCCESS);
}
