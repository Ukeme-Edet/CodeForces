/**
 * @file 977a_ws.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Wrong Subtraction(https://codeforces.com/contest/977/problem/A)
 * @version 0.1
 * @date 2024-03-15
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
	int n;
	short k;
	cin >> n >> k;
	while (k--)
		n % 10 == 0 ? n /= 10 : n--;
	cout << n;
	return (EXIT_SUCCESS);
}
