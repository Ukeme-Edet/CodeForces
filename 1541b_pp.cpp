#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	long long prod;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vector<pair<int, int>> a(n);
		for (int i = 0; i < n; i++)
		{
			cin >> a[i].first;
			a[i].second = i;
		}
		sort(a.begin(), a.end());
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				prod = (long long)a[i].first * a[j].first;
				if (prod > 2 * n)
					break;
				if (a[i].second + a[j].second == prod - 2)
					++ans;
			}
		}
		cout << ans << '\n';
	}
}
