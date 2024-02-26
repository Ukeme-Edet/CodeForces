/**
 * @file 1931a_rass.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Recovering a Small String(https://codeforces.com/problemset/problem/1931/A)
 * @version 0.1
 * @date 2024-02-26
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
	short t, n, i, j, k;
	string temp;
	vector<string> sp(78, "");

	for (i = 0; i < 26; i++)
		for (j = 0; j < 26; j++)
			for (k = 0; k < 26; k++)
			{
				temp = "";
				temp += static_cast<char>(i + 97);
				temp += static_cast<char>(j + 97);
				temp += static_cast<char>(k + 97);
				if (sp[i + j + k + 2] == "")
					sp[i + j + k + 2] = temp;
			}
	cin >> t;
	while (t--)
	{
		cin >> n;
		cout << sp[n - 1] << '\n';
	}
	return (EXIT_SUCCESS);
}
