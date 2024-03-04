/**
 * @file 1904a_forked.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Forked!(https://codeforces.com/problemset/problem/1904/A)
 * @version 0.1
 * @date 2024-03-05
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
	short t, ans;
	;
	int a, b, xk, yk, xq, yq;
	vector<pair<short, short>> directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}, {0, 0}};
	set<pair<int, int>> kap, qap;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> xk >> yk >> xq >> yq;
		ans = 0;
		kap.clear();
		qap.clear();
		for (pair<int, int> direction : directions)
		{
			kap.insert({xk + direction.first * a, yk + direction.second * b});
			qap.insert({xq + direction.first * a, yq + direction.second * b});
		}
		for (pair<int, int> direction : directions)
		{
			kap.insert({xk + direction.first * b, yk + direction.second * a});
			qap.insert({xq + direction.first * b, yq + direction.second * a});
		}
		for (pair<int, int> kapi : kap)
			qap.find(kapi) != qap.end() ? ans++ : ans;
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
