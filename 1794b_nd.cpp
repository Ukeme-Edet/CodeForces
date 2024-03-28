/**
 * @file 1794b_nd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Not Dividing(https://codeforces.com/contest/1794/problem/B)
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
	short t, n;
	int curr, prev, i;

	cin >> t;
	while (t--)
	{
		cin >> n >> prev;
		prev == 1 ? cout << "2 " : cout << prev << ' ';
		prev == 1 ? prev = 2 : prev;
		for (i = 1; i < n; i++)
		{
			cin >> curr;
			if (curr == 1)
				curr++;
			if (!(curr % prev))
				curr++;
			cout << curr << ' ';
			prev = curr;
		}
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
