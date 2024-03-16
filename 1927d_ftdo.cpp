/**
 * @file 1927d_ftdo.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Find the Different Ones!(Find the Different Ones!)
 * @version 0.1
 * @date 2024-04-03
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
	int n, q, l, r;
	vector<int> a, b;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		b.resize(n);
		for (int &ai : a)
			cin >> ai;
		b[0] = -1;
		for (l = 1; l < n; l++)
			a[l] != a[l - 1] ? b[l] = l - 1 : b[l] = b[l - 1];
		cin >> q;
		while (q--)
		{
			cin >> l >> r;
			r--, l--;
			b[r] != -1 && b[r] != b[l] ? cout << b[r] + 1 << ' ' << r + 1 << '\n' : cout << "-1 -1\n";
		}
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
