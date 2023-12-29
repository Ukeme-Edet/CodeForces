#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, a, b, c;
	cin >> t;
	while (t--)
	{
		cin >> a >> b >> c;
		a == b ? cout << c << "\n" : (b == c ? cout << a << "\n" : cout << b << "\n");
	}
}