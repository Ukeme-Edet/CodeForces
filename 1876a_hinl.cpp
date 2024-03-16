/**
 * @file 1876a_hinl.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Helmets in Night Light(https://codeforces.com/problemset/problem/1876/A)
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
	short t;
	int n, p, i;
	long long cost;
	vector<pair<int, int>> kc;

	cin >> t;
	while (t--)
	{
		cin >> n >> p;
		kc.resize(n);
		cost = p;
		n--;
		for (pair<int, int> &kci : kc)
			cin >> kci.second;
		for (pair<int, int> &kci : kc)
			cin >> kci.first;
		sort(kc.begin(), kc.end());
		i = 0;
		while (n && kc[i].first < p)
		{
			cost += (long long)kc[i].first * min(kc[i].second, n);
			n -= min(kc[i].second, n);
			i++;
		}
		if (n)
			cost += (long long)p * n;
		cout << cost << '\n';
	}
	return (EXIT_SUCCESS);
}
