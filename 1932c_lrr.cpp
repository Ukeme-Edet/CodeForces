/**
 * @file 1932c_lrr.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem LR-remainders(https://codeforces.com/contest/1932/problem/C)
 * @version 0.1
 * @date 2024-04-03
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
	short t, m;
	int n, l, r, i;
	vector<short> a, b;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> m;
		a.resize(n);
		b.resize(n);
		for (short &ai : a)
			cin >> ai;
		cin >> s;
		l = 0, r = n - 1;
		for (i = 0; i < n - 1; i++)
			s[i] == 'L' ? l++ : r--;
		b[n - 1] = a[l] % m;
		for (i = n - 2; i > -1; i--)
			b[i] = s[i] == 'L' ? (b[i + 1] * a[--l]) % m : (b[i + 1] * a[++r]) % m;
		for (short bi : b)
			cout << bi << ' ';
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
