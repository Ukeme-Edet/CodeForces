/**
 * @file 1772c_dd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution for codeforces 1772C (https://codeforces.com/problemset/problem/1772/C)
 * @version 0.1
 * @date 2024-01-29
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
	short t, n, k, i, d, in;
	vector<short> a;

	cin >> t;
	while (t--)
	{
		d = 1;
		cin >> k >> n;
		a.resize(k);
		a[0] = 1;
		a[1] = 2;
		in = n;
		for (i = 3; i <= k; i++)
		{
			a[i - 1] = a[i - 2] + 1;
			if (n - k >= d)
			{
				a[i - 1] += d;
				n -= d;
				d++;
			}
		}
		a[k - 1] = in;
		for (auto i : a)
			cout << i << " ";
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
