/**
 * @file 1878c_vic.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vasilije in Cacak(https://codeforces.com/problemset/problem/1878/C)
 * @version 0.1
 * @date 2024-03-17
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
	int n, k;
	long long x;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> x;
		((long long)n * (n + 1) / 2.0 >= x &&											 // check if the sum of the first n natural numbers is greater than or equal to x
		 (long long)k * (k + 1) / 2.0 <= x &&											 // check if the sum of the first k natural numbers is less than or equal to x
		 ((long long)n * (n + 1) / 2.0) - ((long long)(n - k) * (n - k + 1) / 2.0) >= x) // check if the sum of the first n natural numbers minus the sum of the first n-k natural numbers is greater than or equal to x
			? cout << "YES\n"
			: cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
