/**
 * @file 1896a_miz.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Make It Zero(https://codeforces.com/problemset/problem/1869/A)
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
	short t, n, temp, i;

	cin >> t;
	while (t--)
	{
		cin >> n;
		for (i = 0; i < n; i++)
			cin >> temp;
		if (n % 2)
		{
			cout << "4\n";
			cout << "1 " << n << "\n1 " << n - 1 << "\n"
				 << n - 1 << ' ' << n << '\n'
				 << n - 1 << " " << n << "\n";
		}
		else
			cout << "2\n"
				 << "1 " << n << "\n1 " << n << "\n";
	}
	return (EXIT_SUCCESS);
}
