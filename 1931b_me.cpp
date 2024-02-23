/**
 * @file 1931b_me.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Make Equal(https://codeforces.com/problemset/problem/1931/B)
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
	int n, e;
	long long sum, exc;
	vector<int> a;

	cin >> t;
l1:
	while (t--)
	{
		cin >> n;
		a.resize(n);
		sum = 0;
		exc = 0;
		e = 0;
		for (int &ai : a)
		{
			cin >> ai;
			sum += ai;
		}
		e = sum / n;
		for (int ai : a)
		{
			exc += ai - e;
			if (exc < 0)
			{
				cout << "NO\n";
				goto l1;
			}
		}
		cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
