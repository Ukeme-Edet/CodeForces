#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short n, ans = 0;
	cin >> n;
	vector<pair<short, short>> p(n);
	bool a[n];
	for (auto &i : p)
		cin >> i.first >> i.second;
	for (short i = 0; i < n; i++)
	{
		a[0] = a[1] = a[2] = a[3] = false;
		for (int j = 0; j < n; j++)
		{
			if (p[i].first == p[j].first)
			{
				if (p[i].second < p[j].second)
					a[0] = true;
				if (p[i].second > p[j].second)
					a[1] = true;
			}
			if (p[i].second == p[j].second)
			{
				if (p[i].first < p[j].first)
					a[2] = true;
				if (p[i].first > p[j].first)
					a[3] = true;
			}
		}
		a[0] && a[1] && a[2] && a[3] ? ans++ : 0;
	}
	cout << ans << "\n";
}