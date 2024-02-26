/**
 * @file 1921c_sm.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Sending Messages(https://codeforces.com/problemset/problem/1921/C)
 * @version 0.1
 * @date 2024-02-26
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
	int n, a, b, last, i, temp;
	long long f;

	cin >> t;
	while (t--)
	{
		cin >> n >> f >> a >> b;
		last = 0;
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			if ((long long)(temp - last) * a > b)
				f -= b;
			else
				f -= (long long)(temp - last) * a;
			last = temp;
		}
		f > 0 ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
