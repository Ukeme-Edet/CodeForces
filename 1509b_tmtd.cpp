#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, mc;
	string s;

	cin >> t;
next:
	while (t--)
	{
		cin >> n >> s;
		vector<int> psl(n + 1, 0), psr(n + 1, 0);
		for (int i = 0; i < n; i++)
		{
			psl[i + 1] = psl[i] + (s[i] == 'T');
			psr[n - i - 1] = psr[n - i] + (s[n - i - 1] == 'T');
		}
		mc = 0;
		for (int i = 0; i < n; i++)
		{
			if (s[i] == 'M')
			{
				mc++;
				if (psl[i] < mc || psr[i + 1] < mc)
				{
					cout << "NO\n";
					goto next;
				}
			}
		}
		psl[n] / 2 == mc ? cout << "YES\n" : cout << "NO\n";
	}
}