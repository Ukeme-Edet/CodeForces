/**
 * @file 1950c_cc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Clock Conversion(http://codeforces.com/contest/1950/problem/C)
 * @version 0.1
 * @date 2024-03-28
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
	short t, h, m;
	string s, p;

	cin >> t;
	while (t--)
	{
		cin >> s;
		h = stoi(s.substr(0, 2));
		m = stoi(s.substr(3, 2));
		p = "AM";
		if (h >= 12)
		{
			p = "PM";
			if (h > 12)
				h -= 12;
		}
		if (h == 0)
			h = 12;
		cout << setfill('0') << setw(2) << h << ':' << setfill('0') << setw(2) << m << ' ' << p << '\n';
	}
	return (EXIT_SUCCESS);
}
