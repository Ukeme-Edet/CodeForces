/**
 * @file 1926d_vad.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vlad and Division(https://codeforces.com/contest/1926/problem/D)
 * @version 0.1
 * @date 2024-03-17
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

string invert_binary_string(string binary_string)
{
	string inverted_string = "";
	for (char ch : binary_string)
	{
		inverted_string += (ch == '0') ? '1' : '0';
	}
	return inverted_string;
}

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
	int n, i, temp, ans;
	map<string, int> bs;
	set<string> ss;
	string invs;

	cin >> t;
	while (t--)
	{
		cin >> n;
		ans = 0;
		bs.clear();
		ss.clear();
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			bs[bitset<31>(temp).to_string()]++;
		}
		ans = 0;
		for (pair<string, int> p : bs)
		{
			invs = invert_binary_string(p.first);
			if (ss.find(p.first) == ss.end() && ss.find(invs) == ss.end())
			{
				ans += max(bs[p.first], bs[invs]);
				ss.insert(p.first);
				ss.insert(invs);
			}
		}
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
