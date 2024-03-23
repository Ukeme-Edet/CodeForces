/**
 * @file 1946a_moaa.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Median of an Array(https://codeforces.com/contest/1946/problem/A)
 * @version 0.1
 * @date 2024-03-23
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
	int n, li, mi, no;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		sort(a.begin(), a.end());
		mi = n / 2 + n % 2 - 1;
		li = upper_bound(a.begin(), a.end(), a[mi]) - a.begin() - 1;
		cout << li - (n / 2 + n % 2 - 1) + 1 << '\n';
	}
	return (EXIT_SUCCESS);
}
