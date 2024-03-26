/**
 * @file 1877a_gov.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Goals of Victory(https://codeforces.com/contest/1877/problem/A)
 * @version 0.1
 * @date 2024-03-26
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
	short t, n;
	vector<short> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n - 1);
		for (short &ai : a)
			cin >> ai;
		cout << reduce(a.begin(), a.end()) * -1 << '\n';
	}
	return (EXIT_SUCCESS);
}
