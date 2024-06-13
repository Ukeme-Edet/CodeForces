/**
 * @file 1845a_fi.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Forbidden Integer(https://codeforces.com/problemset/problem/1845/A)
 * @version 0.1
 * @date 2024-06-13
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * Repeats a given string `n` times.
 *
 * @param s The string to be repeated.
 * @param n The number of times to repeat the string.
 * @return The resulting string after repeating `s` `n` times.
 */
string repeat(string s, int n)
{
	string s1 = "";

	for (int i = 0; i < n; i++)
		s1 += s;
	return s1;
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n, k, x;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> x;
		if (x != 1 || ((n % 2 && k > 2) || (n % 2 == 0 && k > 1)))
		{
			cout << "YES\n";
			if (x != 1)
				cout << n << '\n'
					 << repeat("1 ", n) << '\n';
			else
			{
				if (n % 2)
					cout << n / 2 << '\n'
						 << "3 " << repeat("2 ", n / 2 - 1) << '\n';
				else
					cout << n / 2 << '\n'
						 << repeat("2 ", n / 2) << '\n';
			}
		}
		else
			cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
