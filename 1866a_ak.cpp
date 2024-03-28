/**
 * @file 1866a_ak.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Ambitious Kid(https://codeforces.com/contest/1866/problem/A)
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
	int n, i, temp, ans;

	cin >> n;
	ans = INT_MAX;
	for (i = 0; i < n; i++)
	{
		cin >> temp;
		ans = min(ans, abs(temp));
	}
	cout << ans << '\n';
	return (EXIT_SUCCESS);
}
