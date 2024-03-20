/**
 * @file 1937a_sp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Shuffle Party(https://codeforces.com/contest/1937/problem/A)
 * @version 0.1
 * @date 2024-03-20
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
	long long n, i;

	cin >> t;
	while (t--)
	{
		cin >> n;
		if (n == 1)
		{
			cout << "1\n";
			continue;
		}
		if (n == 2)
		{
			cout << "2\n";
			continue;
		}
		i = 2;
		while (i * 2 <= n)
			i *= 2;
		cout << i << '\n';
	}
	return (EXIT_SUCCESS);
}
