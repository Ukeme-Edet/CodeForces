/**
 * @file 1859a_uws.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem United We Stand(https://codeforces.com/problemset/problem/1859/A)
 * @version 0.1
 * @date 2024-06-07
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
	unsigned short t, n, i;
	vector<unsigned> a, b, c;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (auto &ai : a)
			cin >> ai;
		sort(a.begin(), a.end());
		b.clear(), c.clear();
		b.push_back(a[0]);
		for (i = 1; i < n; i++)
			if (!(b[0] % a[i]))
				b.push_back(a[i]);
			else
				c.push_back(a[i]);
		if (b.size() && c.size())
		{
			cout << b.size() << ' ' << c.size() << '\n';
			for (i = 0; i < b.size(); i++)
				cout << b[i] << ' ';
			cout << '\n';
			for (i = 0; i < c.size(); i++)
				cout << c[i] << ' ';
			cout << '\n';
		}
		else
			cout << "-1\n";
	}
	return (EXIT_SUCCESS);
}
