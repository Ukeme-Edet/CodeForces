/**
 * @file 1950d_pobd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Product of Binary Decimals(http://codeforces.com/contest/1950/problem/D)
 * @version 0.1
 * @date 2024-04-01
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

void prod(int n, vector<int> &bd, map<int, bool> &bdp)
{
	if (n > 100000)
	{
		return;
	}
	bdp[n] = 1;
	for (int i = 0; i < bd.size(); i++)
		prod(n * bd[i], bd, bdp);
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t, n, i, ic;
	vector<int> bd;
	map<int, bool> bdp;

	for (i = 10; i < 100001; i++)
	{
		ic = i;
		while (ic)
		{
			if (ic % 10 != 0 && ic % 10 != 1)
			{
				goto next;
			}
			ic /= 10;
		}
		bd.push_back(i);
		bdp[i] = 1;
	next:;
	}
	prod(1, bd, bdp);
	cin >> t;
	while (t--)
	{
		cin >> n;
		bdp[n] ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
