/**
 * @file 1945c_larh.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Left and Right Houses(https://codeforces.com/contest/1945/problem/C)
 * @version 0.1
 * @date 2024-03-19
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
	int n, co, cz, ans;
	double tr;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		cz = 0;
		co = count(s.begin(), s.end(), '1');
		tr = DBL_MAX;
		for (int i = 0; i < n; i++)
		{
			if (s[i] == '1')
				co--;
			else
				cz++;
			if (cz >= ceil((i + 1) / 2.0) && co >= ceil((n - i - 1) / 2.0) && tr > abs(n / 2.0 - i - 1))
			{
				tr = abs(n / 2.0 - i - 1);
				ans = i + 1;
			}
		}
		if (count(s.begin(), s.end(), '1') >= ceil(n / 2.0) && n / 2.0 <= tr)
			cout << "0\n";
		else
			cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
