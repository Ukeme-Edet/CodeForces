#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n, m;
	long long ans;
	cin >> t;
	while (t--)
	{
		cin >> n >> m;
		vector<int> a(n);
		for (short i = 0; i < n; i++)
			cin >> a[i];
		vector<int> b(m);
		for (short i = 0; i < m; i++)
			cin >> b[i];
		for (short i = 0; i < m; i++)
		{
			sort(a.begin(), a.end());
			a[0] = b[i];
		}
		cout << (long long)reduce(a.begin(), a.end(), 0LL) << '\n';
	}
}