/**
 * @file 1858a_buttons.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Buttons(https://codeforces.com/problemset/problem/1858/A)
 * @version 0.1
 * @date 2024-06-07
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
	unsigned int a, b, c;

	cin >> t;
	while (t--)
	{
		cin >> a >> b >> c;
		a += c / 2 + (c % 2);
		b += c / 2;
		a > b ? cout << "First\n" : cout << "Second\n";
	}
	return (EXIT_SUCCESS);
}
