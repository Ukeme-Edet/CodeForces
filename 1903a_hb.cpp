/**
 * @file 1903a_hb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Halloumi Boxes(https://codeforces.com/problemset/problem/1903/A)
 * @version 0.1
 * @date 2024-03-15
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
	short t, k, n;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		k == 1 && !is_sorted(a.begin(), a.end()) ? cout << "NO\n" : cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
