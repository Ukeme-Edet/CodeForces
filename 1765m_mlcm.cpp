/**
 * @file 1765m_mlcm.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Minimum LCM(https://codeforces.com/contest/1765/problem/M)
 * @version 0.1
 * @date 2024-03-27
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
	int n, f, g;

	cin >> t;
	while (t--)
	{
		cin >> n;
		f = 1;
		for (g = 2; g * g <= n; g++)
		{
			if (n % g == 0)
			{
				f = n / g;
				break;
			}
		}
		cout << f << ' ' << n - f << '\n';
	}
	return (EXIT_SUCCESS);
}
