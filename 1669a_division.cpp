#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	cin >> t;
	for (short i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		cout << "Division ";
		if (n >= 1900)
			cout << "1\n";
		else if (1600 <= n && n < 1900)
			cout << "2\n";
		else if (1400 <= n && n < 1600)
			cout << "3\n";
		else
			cout << "4\n";
	}
}