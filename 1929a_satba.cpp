/**
 * @file 1929a_satba.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Sasha and the Beautiful Array(https://codeforces.com/problemset/problem/1929/A)
 * @version 0.1
 * @date 2024-03-05
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
	short t, n, i;
	int ans;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		ans = 0;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		sort(a.begin(), a.end());
		for (i = 1; i < n; i++)
			ans += a[i] - a[i - 1];
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
