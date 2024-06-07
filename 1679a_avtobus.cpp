/**
 * @file 1679a_avtobus.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem AvtoBus(https://codeforces.com/problemset/problem/1679/A)
 * @version 0.1
 * @date 2024-06-07
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
	unsigned short t;
	long long n, n6, n4;

	cin >> t;
	while (t--)
	{
		cin >> n;
		if (n % 2 || n < 4)
		{
			cout << "-1\n";
			continue;
		}
		n6 = n / 6, n4 = (n % 6) / 4;
		while (n6 * 6 + n4 * 4 != n && n6 > -1)
		{
			n6--;
			n4 = (n - (n6 * 6)) / 4;
		}
		cout << n6 + n4 << ' ';
		n4 = n / 4, n6 = 0;
		while (n6 * 6 + n4 * 4 != n && n4 > -1)
		{
			n4--;
			n6 = (n - (n4 * 4)) / 6;
		}
		cout << n4 + n6 << '\n';
	}
	return (EXIT_SUCCESS);
}
