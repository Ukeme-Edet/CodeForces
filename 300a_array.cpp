#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short int n, c0, cn;
	cin >> n;
	vector<short int> a(n);
	for (auto i = 0; i < n; i++)
		cin >> a[i];
	sort(a.begin(), a.end());
	cout << 1 << " " << a[0] << "\n";
	if (a[a.size() - 1] > 0)
	{
		cout << 1 << " " << a[a.size() - 1] << "\n";
		cout << n - 2 << " ";
		for (auto i = 1; i < n - 1; i++)
			cout << a[i] << " ";
	}
	else
	{
		cout << 2 << " " << a[1] << " " << a[2] << "\n";
		cout << n - 3 << " ";
		for (auto i = 3; i < n; i++)
			cout << a[i] << " ";
	}
	cout << "\n";
}