/**
 * @file 1855b_ldi.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Longest Divisors Interval(https://codeforces.com/problemset/problem/1855/B)
 * @version 0.1
 * @date 2024-03-19
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
		i = 1;
		while (n % i == 0)
			i++;
		cout << i - 1 << '\n';
	}
	return (EXIT_SUCCESS);
}
