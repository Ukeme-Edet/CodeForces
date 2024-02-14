/**
 * @file 1931c_mea.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 1931C - Make Equal Again(https://codeforces.com/problemset/problem/1931/C)
 * @version 0.1
 * @date 2024-02-14
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
	int n, f, b, i;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		f = b = i = 0;
		while (i < n && a[i++] == a[0])
			f++;
		i = n - 1;
		while (i > -1 && a[i--] == a[n - 1])
			b++;
		cout << (a[0] == a[n - 1] ? max(n - f - b, 0) : n - max(f, b)) << '\n';
	}
	return (EXIT_SUCCESS);
}
