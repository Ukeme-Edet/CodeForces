#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short n, c = 0;
	string s;
	cin >> n >> s;
	for (short i = 1; i < n; i++)
		if (s[i] == s[i - 1])
			c++;
	cout << c << "\n";
}