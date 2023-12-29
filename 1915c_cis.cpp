#include <bits/stdc++.h>

using namespace std;

bool is_square(long long n)
{
	long long tmp = sqrt(n);
	return tmp * tmp == n;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, tmp;
	long long ans;
	cin >> t;
	while (t--)
	{
		cin >> n;
		ans = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> tmp;
			ans += tmp;
		}
		is_square(ans) ? cout << "YES\n" : cout << "NO\n";
	}
}