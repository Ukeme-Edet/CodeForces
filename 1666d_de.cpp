/**
 * @file 1666d_de.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Deletive Editing(https://codeforces.com/problemset/problem/1666/D)
 * @version 0.1
 * @date 2024-06-13
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
	short n, i, v;
	string s, t;
	map<char, bool> seen;

	cin >> n;
	while (n--)
	{
		cin >> s >> t;
		reverse(s.begin(), s.end());
		reverse(t.begin(), t.end());
		seen.clear();
		i = v = 0;
		for (char c : t)
		{
			for (; i < s.size(); i++)
			{
				if (s[i] == c)
				{
					if (!seen[c])
						v++, i++;
					break;
				}
				else
					seen[s[i]] = true;
			}
		}
		v == t.size() ? cout << "YES\n" : cout << "NO\n";
	}
	return (EXIT_SUCCESS);
}
