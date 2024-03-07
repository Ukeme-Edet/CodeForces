/**
 * @file 1913b_sad.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Swap and Delete(https://codeforces.com/problemset/problem/1913/B)
 * @version 0.1
 * @date 2024-03-15
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
	int oc, zc, i;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> s;
		oc = count(s.begin(), s.end(), '1');
		zc = s.length() - oc;
		i = 0;
		while (i < s.length())
		{
			if (s[i] == '1' && zc > 0)
				zc--;
			else if (s[i] == '0' && oc > 0)
				oc--;
			else
				break;
			i++;
		}
		cout << s.length() - i << '\n';
	}

	return (EXIT_SUCCESS);
}
