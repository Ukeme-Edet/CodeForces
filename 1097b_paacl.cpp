#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	vector<int> v(n);
	for (auto i = 0; i < n; i++)
		cin >> v[i];
	for (auto i = 0; i < pow(2, n); i++)
	{
		bitset<15> binaryRepersentation(i);
		auto sum = 0;
		for (auto j = 0; j < n; j++)
			if (binaryRepersentation[j])
				sum += v[j];
			else
				sum -= v[j];
		if (sum % 360 == 0)
		{
			cout << "YES\n";
			return 0;
		}
	}
	cout << "NO\n";
}