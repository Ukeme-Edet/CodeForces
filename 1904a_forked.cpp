/**
 * @file 1904a_forked.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Forked!(https://codeforces.com/problemset/problem/1904/A)
 * @version 0.1
 * @date 2024-03-14
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
	short t, i, ans;
	int a, b, xk, yk, xq, yq;
	vector<pair<short, short>> directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
	set<pair<short, short>> posk, posq;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> xk >> yk >> xq >> yq;
		posk.clear();
		posq.clear();
		ans = 0;
		for (i = 0; i < 4; i++)
		{
			posk.insert({xk + a * directions[i].first, yk + b * directions[i].second});
			posq.insert({xq + a * directions[i].first, yq + b * directions[i].second});
		}
		for (i = 0; i < 4; i++)
		{
			posk.insert({xk + b * directions[i].first, yk + a * directions[i].second});
			posq.insert({xq + b * directions[i].first, yq + a * directions[i].second});
		}
		for (pair<short, short> posk_en : posk)
			posq.find(posk_en) != posq.end() ? ans++ : 0;
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
