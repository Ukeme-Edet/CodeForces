/**
 * @file 1862b_sg.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Sequence Game(https://codeforces.com/problemset/problem/1862/B)
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
	vector<int> b, a;

	cin >> t;
	while (t--)
	{
		cin >> n;
		b.resize(n);
		a.resize(0);
		for (int &bi : b)
			cin >> bi;
		a.push_back(b[0]);
		for (i = 1; i < n; i++)
		{
			a.push_back(b[i]);
			if (b[i] < b[i - 1])
				a.push_back(b[i]);
		}
		cout << a.size() << '\n';
		for (int ai : a)
			cout << ai << ' ';
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
