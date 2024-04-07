/**
 * @file 1933a_tpran.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Turtle Puzzle: Rearrange and Negate(https://codeforces.com/contest/1933/problem/A)
 * @version 0.1
 * @date 2024-02-27
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
	short t, n, i, temp, ans;

	cin >> t;
	while (t--)
	{
		cin >> n;
		ans = 0;
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			ans += abs(temp);
		}
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
