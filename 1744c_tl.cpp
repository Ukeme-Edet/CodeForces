/**
 * @file 1744c_tl.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Traffic Light(https://codeforces.com/contest/1744/problem/C)
 * @version 0.1
 * @date 2024-03-27
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief This is the main function
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, ans, ng, i;
	string s;
	char c;

	cin >> t;
	while (t--)
	{
		cin >> n >> c >> s;
		ans = 0;
		s[n - 1] == 'g' ? ng = 0 : ng = find(s.begin(), s.end(), 'g') - s.begin();
		for (i = n - 1; i > -1; i--)
		{
			s[i] == 'g' ? ng = 0 : ng++;
			if (s[i] == c)
				ans = max(ans, ng);
		}
		cout << ans << '\n';
	}
	return (0);
}
