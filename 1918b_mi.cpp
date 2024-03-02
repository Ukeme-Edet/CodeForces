/**
 * @file 1918b_mi.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Minimize Inversions(https://codeforces.com/problemset/problem/1918/B)
 * @version 0.1
 * @date 2024-03-02
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
	int n, i;
	vector<pair<int, int>> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (i = 0; i < n; i++)
			cin >> a[i].first;
		for (i = 0; i < n; i++)
			cin >> a[i].second;
		sort(a.begin(), a.end());
		for (i = 0; i < n; i++)
			cout << a[i].first << ' ';
		cout << '\n';
		for (i = 0; i < n; i++)
			cout << a[i].second << ' ';
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
