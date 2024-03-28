/**
 * @file 1725b_bt.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Basketball Together(http://codeforces.com/contest/1725/problem/B)
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
	int n, d, i, ts, nc, wins;
	vector<int> p;

	cin >> n >> d;
	p.resize(n);
	for (int &pi : p)
		cin >> pi;
	sort(p.rbegin(), p.rend());
	wins = 0, nc = n;
	for (i = 0; i < n; i++, wins++)
	{
		ts = ceil((double)d / p[i]);
		!(d % p[i]) ? ts++ : ts;
		if (nc - ts < 0)
			break;
		nc -= ts;
	}
	cout << wins << '\n';
	return (EXIT_SUCCESS);
}
