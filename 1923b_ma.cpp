/**
 * @file 1923b_ma.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Monsters Attack!(https://codeforces.com/contest/1923/problem/B)
 * @version 0.1
 * @date 2024-03-18
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
	long long n, k, last, next;
	vector<pair<long, long>> a;

	cin >> t;
end:
	while (t--)
	{
		cin >> n >> k;
		a.resize(n);
		for (auto &ai : a)
			cin >> ai.first;
		for (auto &ai : a)
		{
			cin >> ai.second;
			ai.second = abs(ai.second);
		}
		sort(a.begin(), a.end(), [](auto &x, auto &y)
			 { return x.second < y.second; });
		last = next = 0;
		for (auto ai : a)
		{
			if (ai.first > k * (ai.second - last) + next)
			{
				cout << "NO\n";
				goto end;
			}
			next += k * (ai.second - last) - ai.first;
			last = ai.second;
		}
		cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
