/**
 * @file 1837b_cs.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Comparison String(https://codeforces.com/problemset/problem/1837/B)
 * @version 0.1
 * @date 2024-03-22
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
	short t, n, ml, l, i;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		ml = l = 1;
		for (i = 1; i < n; i++)
		{
			if (s[i] == s[i - 1])
				l++;
			else
			{
				ml = max(ml, l);
				l = 1;
			}
		}
		ml = max(ml, l);
		cout << ml + 1 << '\n';
	}
	return (EXIT_SUCCESS);
}
