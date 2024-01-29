#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, k, x, sum, i;

	cin >> t;
	while (t--)
	{
		cin >> n >> k >> x;
		vector<short> a(n);
		vector<short> dp(n + 1);
		sum = 0;
		for (short &i : a)
			cin >> i;
		sort(a.rbegin(), a.rend());
		for (i = 0; i < n; i++)
			dp[i + 1] = dp[i] + a[i];
		for (i = 0; i < n; i++)
		
	}
}