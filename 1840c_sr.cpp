/**
 * @file 1840c_sr.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Ski Resort(https://codeforces.com/contest/1840/problem/C)
 * @version 0.1
 * @date 2024-03-19
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
	int n, k, q, temp, i, l;
	long long nw;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> q;
		l = nw = 0;
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			if (temp > q)
			{
				if (l >= k)
					nw += (long long)(l - k + 1) * (l - k + 2) / 2;
				l = 0;
			}
			else
				l++;
		}
		if (l >= k)
			nw += (long long)(l - k + 1) * (l - k + 2) / 2;
		cout << nw << '\n';
	}
	return (EXIT_SUCCESS);
}
