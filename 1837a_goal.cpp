/**
 * @file 1837a_goal.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Grasshopper on a Line(https://codeforces.com/problemset/problem/1837/A)
 * @version 0.1
 * @date 2024-06-13
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
	short t, x, k;

	cin >> t;
	while (t--)
	{
		cin >> x >> k;
		if (!(x % k))
			cout << 2 << '\n'
				 << x - 1 << ' ' << 1 << '\n';
		else
			cout << 1 << '\n'
				 << x << '\n';
	}
	return (EXIT_SUCCESS);
}
