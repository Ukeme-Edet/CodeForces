/**
 * @file 1873g_abbcobacb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem ABBC or BACB(https://codeforces.com/contest/1873/problem/G)
 * @version 0.1
 * @date 2024-03-27
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
	int sl, l, i;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> s;
		if (s[0] == 'B' || s[s.size() - 1] == 'B' || s.find("BB") != string::npos)
		{
			cout << count(s.begin(), s.end(), 'A') << '\n';
			continue;
		}
		l = 0;
		sl = INT_MAX;
		for (i = 0; i < s.size(); i++)
		{
			if (s[i] == 'A')
				l++;
			else
			{
				sl = min(sl, l);
				l = 0;
			}
		}
		sl = min(sl, l);
		s.find('B') != string::npos ? cout << count(s.begin(), s.end(), 'A') - sl << '\n' : cout << "0\n";
	}
	return (EXIT_SUCCESS);
}
