/**
 * @file 151a_sd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 151A - Soft Drinking(https://codeforces.com/problemset/problem/151/A)
 * @version 0.1
 * @date 2024-01-30
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
	short n, k, l, c, d, p, nl, np;

	cin >> n >> k >> l >> c >> d >> p >> nl >> np;
	cout << min({(k * l) / nl, c * d, p / np}) / n << '\n';
	return (EXIT_SUCCESS);
}
