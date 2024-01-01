#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int p;
	string s;
	int cost;
	cin >> t;
	while (t--)
	{
		cin >> s >> p;
		cost = 0;
		vector<pair<char, int>> v(s.size());
		for (auto i = 0; i < s.size(); i++)
		{
			v[i] = {s[i], i};
			cost += (int)s[i] - 96;
		}
		sort(v.begin(), v.end(), [](pair<char, int> a, pair<char, int> b)
			 { return (a.first > b.first); });
		for (auto i = 0; i < v.size() && cost > p; i++)
		{
			cost -= (int)v[i].first - 96;
			v[i].first = 0;
		}
		sort(v.begin(), v.end(), [](pair<char, int> a, pair<char, int> b)
			 { return (a.second < b.second); });
		for (auto i = 0; i < v.size(); i++)
			v[i].first ? cout << v[i].first : cout << "";
		cout << '\n';
	}
}