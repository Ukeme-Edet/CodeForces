/**
 * @file 1926c_vaasosod.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vlad and a Sum of Sum of Digits(https://codeforces.com/contest/1926/problem/C)
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
	short t;
	int n, i, pi, sd;
	int ds[200001] = {0};

	for (i = 1; i < 200001; i++)
	{
		pi = i;
		sd = 0;
		while (pi)
		{
			sd += pi % 10;
			pi /= 10;
		}
		ds[i] = ds[i - 1] + sd;
	}

	cin >> t;
	while (t--)
	{
		cin >> n;
		cout << ds[n] << '\n';
	}
	return (EXIT_SUCCESS);
}
