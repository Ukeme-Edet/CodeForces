#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n;
	long long ans;
	cin >> t;
	while (t--)
	{
		ans = 0;
		cin >> n;
		vector<pair<int, int>> r(n);
		for (auto &p : r)
			cin >> p.first >> p.second;
		// vector<pair<int, int>> rc = r;
		// sort(r.begin(), r.end(), [](pair<int, int> a, pair<int, int> b)
		// 	 { return a.first < b.first; });
		// sort(rc.begin(), rc.end(), [](pair<int, int> a, pair<int, int> b)
		// 	 { return a.second < b.second; });
		// for (int i = 0; i < n; i++)
	}
}