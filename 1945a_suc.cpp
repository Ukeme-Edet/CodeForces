/**
 * @file 1945a_suc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Setting up Camp(https://codeforces.com/contest/1945/problem/0)
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
	int a, b, c, ans;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> c;
		if (b % 3 && 3 - (b % 3) > c)
		{
			cout << "-1\n";
			continue;
		}
		ans = a + (b / 3) + ((b % 3 + c) / 3);
		(b % 3 + c) % 3 ? ans++ : ans;
		cout << ans << "\n";
	}
	return (EXIT_SUCCESS);
}
