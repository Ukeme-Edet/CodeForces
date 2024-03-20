/**
 * @file 1945b_fireworks.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Fireworks(https://codeforces.com/contest/1945/problem/B)
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
	short t;
	long long a, b, m, ans, mt;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> m;
		cout << 2 + m / a + m / b << '\n';
	}
	return (EXIT_SUCCESS);
}
