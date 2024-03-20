/**
 * @file 1831b_am.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Array merging(https://codeforces.com/contest/1831/problem/B)
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
	short t;
	int n, la, lb, i, ans;
	vector<int> a, b;
	map<int, int> ma, mb;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		b.resize(n);
		ma.clear();
		mb.clear();
		for (int &ai : a)
			cin >> ai;
		for (int &bi : b)
			cin >> bi;
		la = lb = 1;
		ans = 0;
		for (i = 1; i < n; i++)
		{
			if (a[i] != a[i - 1])
			{
				ma[a[i - 1]] = max(ma[a[i - 1]], la);
				la = 1;
			}
			else
				la++;
			if (b[i] != b[i - 1])
			{
				mb[b[i - 1]] = max(mb[b[i - 1]], lb);
				lb = 1;
			}
			else
				lb++;
		}
		ma[a[i - 1]] = max(ma[a[i - 1]], la);
		mb[b[i - 1]] = max(mb[b[i - 1]], lb);
		for (auto &p : ma)
			ans = max(ans, p.second + mb[p.first]);
		for (auto &p : mb)
			ans = max(ans, p.second + ma[p.first]);
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
