#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short n;
	cin >> n;
	vector<string> v(n);

	for (auto &x : v)
		cin >> x;
	for (short i = 0; i < n; i++)
	{
		if (v[i][i] != v[0][0])
		{
			cout << "NO\n";
			return (0);
		}
	}
	for (short i = 0; i < n; i++)
	{
		if (v[i][n - i - 1] != v[0][n - 1])
		{
			cout << "NO\n";
			return (0);
		}
	}
	for (short i = 0; i < n; i++)
	{
		for (short j = 0; j < n; j++)
		{
			if (i == j || i == n - j - 1)
				continue;
			if (v[i][j] != v[0][1])
			{
				cout << "NO\n";
				return (0);
			}
		}
	}
	v[0][0] != v[0][1] ? cout << "YES\n" : cout << "NO\n";
}