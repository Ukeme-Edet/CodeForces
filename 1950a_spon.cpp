/**
 * @file 1950a_spon.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Stair, Peak, or Neither?(https://codeforces.com/contest/1950/problem/A)
 * @version 0.1
 * @date 2024-03-28
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
	short t, a, b, c;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> c;
		if (a < b && b < c)
			cout << "STAIR\n";
		else if (a < b && b > c)
			cout << "PEAK\n";
		else
			cout << "NONE\n";
	}
	return (EXIT_SUCCESS);
}
