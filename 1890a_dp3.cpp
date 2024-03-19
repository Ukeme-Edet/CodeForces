/**
 * @file 1890a_dp3.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Doremy's Paint 3(https://codeforces.com/problemset/problem/1890/A)
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
	short t, n, i, c;
	vector<int> a;
	map<int, short> m;

	cin >> t;
	while (t--)
	{
		cin >> n;
		c = 0;
		m.clear();
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		for (i = 0; i < n; i++)
		{
			m[a[i]]++;
			if (a[i] != a[0])
				continue;
			c++;
		}
		if (c == n)
		{
			cout << "Yes\n";
			continue;
		}
		if (m.size() != 2)
			cout << "No\n";
		else
		{
			if (abs(m.begin()->second - next(m.begin())->second) > 1)
				cout << "No\n";
			else
				cout << "Yes\n";
		}
	}
	return (EXIT_SUCCESS);
}
