/**
 * @file 1690d_baws.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Black and White Stripe(https://codeforces.com/problemset/problem/1690/D)
 * @version 0.1
 * @date 2024-06-08
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
	unsigned int n, k, l, r, ans, wc;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> s;
		l = 0, r = 0, wc = s[0] == 'W';
		while (r < n && r - l + 1 < k)
			wc += s[++r] == 'W';
		ans = wc;
		while (r < n - 1)
		{
			s[++r] == 'W' ? wc++ : 0;
			s[l++] == 'W' ? wc-- : 0;
			ans = min(ans, wc);
		}
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
