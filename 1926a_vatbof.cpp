/**
 * @file 1926a_vatbof.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vlad and the Best of Five(https://codeforces.com/problemset/problem/1926/A)
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
	string s;

	cin >> t;
	while (t--)
	{
		cin >> s;
		count(s.begin(), s.end(), 'A') > 2 ? cout << "A\n" : cout << "B\n";
	}
	return (EXIT_SUCCESS);
}
