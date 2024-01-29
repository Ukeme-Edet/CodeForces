#include <bits/stdc++.h>

using namespace std;

int most_xp(int k, vector<pair<short, bool>> &a, vector<short> &b, unordered_map<int, int> &dp)
{
	if (k == 0)
		return (0);
	if (dp.find(k) != dp.end())
		return (dp[k]);
	int ans = 0;
	for (int i = 0; i < a.size(); i++)
	{
		if (a[i].second)
			continue;
		a[i].second = true;
		ans = max(ans, b[i] + most_xp(k - 1, a, b, dp));
		a[i].second = false;
	}
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
	int n, k;
	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		vector<pair<short, bool>> a(n);
		vector<short> b(n);
		unordered_map<int, int> dp;
		for (auto &i : a)
			cin >> i.first;
		for (auto &i : b)
			cin >> i;
		cout << most_xp(k, a, b, dp) << '\n';
	}
	return (EXIT_SUCCESS);
}