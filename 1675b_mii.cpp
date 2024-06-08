/**
 * @file 1675b_mii.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Make It Increasing(https://codeforces.com/problemset/problem/1675/B)
 * @version 0.1
 * @date 2024-06-08
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
	short t, n, i, c;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		c = 0;
		for (i = a.size() - 2; i > -1; i--)
		{
			while ((a[i] || a[i + 1] != 0) && a[i] >= a[i + 1])
				a[i] /= 2, c++;
			if (a[i] >= a[i + 1])
				break;
		}
		i > -1 ? cout << "-1\n" : cout << c << '\n';
	}
	return (EXIT_SUCCESS);
}
