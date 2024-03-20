/**
 * @file 1881a_dttc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Don't Try to Count(https://codeforces.com/contest/1881/problem/A)
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
	short t, n, m, i;
	string x, s;

	cin >> t;
	while (t--)
	{
		cin >> n >> m >> x >> s;
		i = 0;
		while (x.length() <= 50)
		{
			if (x.find(s) != string::npos)
			{
				cout << i << '\n';
				break;
			}
			x += x;
			i++;
		}
		if (x.length() > 50)
		{
			cout << -1 << '\n';
		}
	}
	return (EXIT_SUCCESS);
}
