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
	short t, n, m, i;
	int r;
	long long ans;

	cin >> t;
	while (t--)
	{
		cin >> n;
		vector<vector<int>> a(n);
		
		ans = 0;
		for (i = 0; i < n; i++)
		{
			cin >> m;
			r = INT_MAX;
			a[i].resize(m);
			for (int &j : a[i])
				cin >> j;
			sort(a[i].begin(), a[i].end());
		}
		sort(a.begin(), a.end(), [](const vector<int> &a, const vector<int> &b)
			 { return a[1] > b[1]; });
		for (i = 0; i < n - 1; i++)
		{
			ans += a[i][1];
			r = min(r, a[i][0]);
		}
		ans += min(a[n - 1][0], r);
		cout << ans << '\n';
	}
	return (EXIT_SUCCESS);
}
