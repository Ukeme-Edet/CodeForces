/**
 * @file 1691b_ss.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Shoe Shuffling(https://codeforces.com/problemset/problem/1691/B)
 * @version 0.1
 * @date 2024-06-08
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
	unsigned short t;
	unsigned int n, i, l;
	vector<unsigned int> s;
	map<unsigned int, queue<unsigned int>> aq;

	cin >> t;
	while (t--)
	{
		cin >> n;
		s.resize(n), i = 1;
		aq.clear();
		for (auto &si : s)
		{
			cin >> si;
			aq[si].push(i++);
		}
		i = 0;
		for (auto &aqi : aq)
		{
			if (aqi.second.size() < 2)
				break;
			i++;
			l = aqi.second.front();
			aqi.second.pop();
			aqi.second.push(l);
		}
		if (i != aq.size())
		{
			cout << "-1\n";
			continue;
		}
		for (auto si : s)
		{
			cout << aq[si].front() << ' ';
			aq[si].pop();
		}
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
