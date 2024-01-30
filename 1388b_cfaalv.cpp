/**
 * @file 1388b_cfaalv.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 1388B - Captain Flint and a Long Voyage(https://codeforces.com/problemset/problem/1388/B)
 * @version 0.1
 * @date 2024-01-30
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
	int n, i;

	cin >> t;
	while (t--)
	{
		cin >> n;
		for (i = 0; i < n - (int)ceil(n / 4.0); i++)
			cout << 9;
		for (; i < n; i++)
			cout << 8;
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
