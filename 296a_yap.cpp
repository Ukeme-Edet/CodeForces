#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short int n, t;
	cin >> n;
	vector<short int> v(1000, 0);
	for (short int i = 0; i < n; i++)
	{
		cin >> t;
		v[--t]++;
	}
	short max_e = *max_element(v.begin(), v.end());
	max_e - 1 > reduce(v.begin(), v.end(), 0) - max_e ? cout << "NO\n" : cout << "YES\n";
}