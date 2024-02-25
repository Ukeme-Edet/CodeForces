/**
 * @file 1927c_ctdo.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Chose the Different Ones!(https://codeforces.com/problemset/problem/1927/C)
 * @version 0.1
 * @date 2024-02-25
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
	int n, m, k, ca, cb, i, temp, s;
	map<int, pair<int, map<int, bool>>> nm;

	cin >> t;
l1:
	while (t--)
	{
		cin >> n >> m >> k;
		ca = cb = s = 0;
		nm.clear();
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			nm[temp].first = nm[temp].first + 1;
			nm[temp].second[1] = true;
		}
		for (i = 0; i < m; i++)
		{
			cin >> temp;
			nm[temp].first = nm[temp].first + 1;
			nm[temp].second[2] = true;
		}
		for (i = 1; i <= k; i++)
		{
			if (nm[i].first == 0)
			{
				cout << "NO\n";
				goto l1;
			}
			if (nm[i].first > 1)
			{
				if (nm[i].second[1] && nm[i].second[2])
					s++;
				else if (nm[i].second[1])
					ca++;
				else
					cb++;
			}
			else
				nm[i].second[2] ? cb++ : ca++;
		}
		max(k / 2 - ca, 0) + max(k / 2 - cb, 0) <= s ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
