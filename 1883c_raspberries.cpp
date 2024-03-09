/**
 * @file 1883c_raspberries.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Raspberries(https://codeforces.com/problemset/problem/1883/C)
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
	short t, k;
	int n, ans, ec, oc;
	vector<int> a;
	bool found;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		found = false;
		ans = ec = oc = 0;
		for (int &ai : a)
		{
			cin >> ai;
			if (ai % k == 0)
				found = true;
			if (k == 2)
				ans = max(ans, ai % 2);
			else if (k == 3)
				ans = max(ans, ai % 3);
			else if (k == 4)
			{
				ans = max(ans, ai % 4);
				ai % 2 ? oc++ : ec++;
			}
			else
				ans = max(ans, ai % 5);
		}
		if (k != 4)
			found ? cout << 0 << '\n' : cout << k - ans << '\n';
		else
		{
			if (found || ec > 1)
				cout << 0 << '\n';
			else if (ec)
				cout << 1 << '\n';
			else
				cout << min(2, k - ans) << '\n';
		}
	}
	return (EXIT_SUCCESS);
}
