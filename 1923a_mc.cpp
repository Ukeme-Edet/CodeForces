/**
 * @file 1923a_mc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Moving Chips(https://codeforces.com/contest/1923/problem/A)
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
	short t, n, x1, x2, w;
	string s, bl;

	cin >> t;
	while (t--)
	{
		cin >> n;
		s = "";
		for (short i = 0; i < n; i++)
		{
			cin >> w;
			s += to_string(w);
		}
		x1 = s.find('1');
		x2 = s.find_last_of('1');
		bl = s.substr(x1, x2 - x1 + 1);
		cout << count(bl.begin(), bl.end(), '0') << '\n';
	}
	return (EXIT_SUCCESS);
}
