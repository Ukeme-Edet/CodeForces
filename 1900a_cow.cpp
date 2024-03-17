/**
 * @file 1900a_cow.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Cover in Water(https://codeforces.com/problemset/problem/1900/A)
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
	short t, n, b;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		b = 0;
		for (char si : s)
			si == '.' ? b++ : 0;
		s.find("...") != string::npos ? cout << "2\n" : cout << b << '\n';
	}
	return (EXIT_SUCCESS);
}
