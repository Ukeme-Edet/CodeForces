/**
 * @file 1927b_fts.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Following the String(https://codeforces.com/problemset/problem/1927/B)
 * @version 0.1
 * @date 2024-02-25
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
	int n, i, j;
	vector<int> a;
	vector<char> s;
	map<char, int> cm;

	cin >> t;
	while (t--)
	{
		cin >> n;
		a.resize(n);
		s.resize(n);
		for (int &ai : a)
			cin >> ai;
		for (i = 0; i < 26; i++)
			cm[97 + i] = 0;
		for (j = 0; j < n; j++)
		{
			for (i = 0; i < 26; i++)
			{
				if (cm[97 + i] == a[j])
				{
					cm[97 + i]++;
					s[j] = 97 + i;
					break;
				}
			}
		}
		for (char si : s)
			cout << si;
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
