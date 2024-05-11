/**
 * @file 1696b_nitdtu.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem NIT Destroys the Universe(https://codeforces.com/problemset/problem/1696/B)
 * @version 0.1
 * @date 2024-05-13
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
	int n, i;
	bool zi;
	vector<int> a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		for (int &ai : a)
			cin >> ai;
		zi = 0;
		if (count(a.begin(), a.end(), 0) == n)
			cout << "0\n";
		else
		{
			i = 0;
			while (i < n && !a[i])
				i++;
			while (i < n && a[i])
				i++;
			while (i < n && !a[i])
				i++;
			zi = i != n;
			zi ? cout << "2\n" : cout << "1\n";
		}
	}
	return (EXIT_SUCCESS);
}
