/**
 * @file 1791d_ds.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Distinct Split(https://codeforces.com/contest/1791/problem/D)
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
	int n, i, ans;
	string s;
	vector<int> dcl, dcr;
	map<char, bool> m;

	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		m.clear();
		dcl.resize(n);
		dcr.resize(n);
		dcl[0] = 1, m[s[0]] = 1;
		for (i = 1; i < n; i++)
		{
			if (m[s[i]])
				dcl[i] = dcl[i - 1];
			else
			{
				dcl[i] = dcl[i - 1] + 1;
				m[s[i]] = 1;
			}
		}
		m.clear();
		dcr[n - 1] = 1, m[s[n - 1]] = 1;
		for (i = n - 2; i > -1; i--)
		{
			if (m[s[i]])
				dcr[i] = dcr[i + 1];
			else
			{
				dcr[i] = dcr[i + 1] + 1;
				m[s[i]] = 1;
			}
		}
		ans = 0;
		for (i = 1; i < n; i++)
			ans = max(ans, dcl[i - 1] + dcr[i]);
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
