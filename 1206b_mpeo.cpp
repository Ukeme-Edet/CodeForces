/**
 * @file 1206b_mpeo.cpp
 * @author UKeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 1206B - Make Product Equal One(https://codeforces.com/problemset/problem/1206/B)
 * @version 0.1
 * @date 2024-01-31
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
	int n, temp, i, j;
	bool zero = false;
	long long ans = 0;
	vector<int> v;

	cin >> n;
	v.resize(n);
	i = 0;
	while (n--)
	{
		cin >> temp;
		if (temp < 0)
			v[i++] = temp;
		else if (temp == 0)
		{
			zero = true;
			ans++;
		}
		else
			ans += temp - 1;
	}
	sort(v.rbegin(), v.rend() - i);
	for (j = 1; j < i; j += 2)
		ans += (-1 * v[j]) + (-1 * v[j - 1]) - 2;
	if (i % 2 && !zero)
		ans += -1 * v[i - 1] + 1;
	else if (i % 2 && zero)
		ans += -1 * v[i - 1] - 1;
	cout << ans;
	return (EXIT_SUCCESS);
}
