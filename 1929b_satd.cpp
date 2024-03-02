/**
 * @file 1929b_satd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Sasha and the Drawing(https://codeforces.com/problemset/problem/1929/B)
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
	long long n, k;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		k > 4 * n - 4 ? cout << k - 2 * n + 2 : cout << (long long)ceil(k / 2.0);
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
