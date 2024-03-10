/**
 * @file 1883b_chemistry.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Chemistry(https://codeforces.com/problemset/problem/1883/B)
 * @version 0.1
 * @date 2024-03-16
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
	int n, k, oc;
	string s;
	map<char, int> sm;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> s;
		oc = 0;
		sm.clear();
		for (char &si : s)
			sm[si]++;
		for (pair<const char, int> &smi : sm)
			oc += smi.second % 2;
		oc - 1 > k ? cout << "NO\n" : cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
