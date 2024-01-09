#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	string s;
	cin >> t;
	while (t--)
	{
		cin >> s;
		for (int i = 0; i < s.size(); i += 2)
		{
			cout << s[i];
		}
		cout << s[s.size() - 1] << '\n';
	}
}