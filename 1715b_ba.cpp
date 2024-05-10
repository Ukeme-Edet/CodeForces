/**
 * @file 1715b_ba.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Beautiful Array(https://codeforces.com/problemset/problem/1715/B)
 * @version 0.1
 * @date 2024-05-13
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
	int n, k, b, i;
	long long s;
	vector<long long> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> b >> s;
		if (1ll * (k - 1) * (n - 1) < (s - ((long long)(1ll * k * b) + k - 1)) || s < (long long)(1ll * k * b))
		{
			cout << "-1\n";
			continue;
		}
		a.resize(n);
		a.assign(n, 0);
		a[0] = min(s, (long long)k * b + k - 1);
		s -= a[0];
		i = 1;
		while (s)
		{
			a[i++] = min(s, (long long)k - 1);
			s -= min((long long)k - 1, s);
		}
		for (long long ai : a)
			cout << ai << ' ';
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
