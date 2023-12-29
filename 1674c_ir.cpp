#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int q;
	string s, t;
	cin >> q;
	while (q--)
	{
		cin >> s >> t;
		if (t == "a")
		{
			cout << 1 << "\n";
			continue;
		}
		if (t.find("a") != string::npos)
		{
			cout << -1 << "\n";
			continue;
		}
		long long ans = 1;
		for (auto i = 0; i < s.size(); i++)
			ans *= 2;
		cout << ans << "\n";
	}
}