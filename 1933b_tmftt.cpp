/**
 * @file 1933b_tmftt.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Turtle Math: Fast Three Task(https://codeforces.com/contest/1933/problem/B)
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
	short t, ai;
	int n, i, oc, tc, sum;

	cin >> t;
	while (t--)
	{
		cin >> n;
		oc = tc = sum = 0;
		for (i = 0; i < n; i++)
		{
			cin >> ai;
			if (ai % 3 == 1)
				oc++;
			if (ai % 3 == 2)
				tc++;
			sum += ai;
		}
		if (!(sum % 3))
			cout << "0\n";
		else if ((sum % 3 == 1 && oc > 0) || (sum % 3 == 2 && tc > 0) || sum % 3 == 2)
			cout << "1\n";
		else
			cout << "2\n";
	}
	return (EXIT_SUCCESS);
}
