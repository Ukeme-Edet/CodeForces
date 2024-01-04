#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n;
	cin >> t;
next2:
	while (t--)
	{
		cin >> n;
		vector<vector<short>> p(n, vector<short>(n - 1, 0));
		for (short i = 0; i < n; i++)
		{
			for (int j = 0; j < n - 1; j++)
			{
				cin >> p[i][j];
			}
		}
		for (short i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (p[i][0] == p[j][0])
				{
					cout << p[i][0] << " ";
					goto next1;
				}
			}
		}
	next1:
		for (short i = 0; i < n - 2; i++)
		{
			bool broke = false;
			for (short j = 0; j < n && !broke; j++)
			{
				for (int k = 0; k < n; k++)
				{
					if (p[j][i] == p[k][i + 1])
					{
						cout << p[j][i] << " ";
						broke = true;
						break;
					}
				}
			}
		}
		for (short i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (p[i][p[i].size() - 1] == p[j][p[j].size() - 1])
				{
					cout << p[i][p[i].size() - 1] << "\n";
					goto next2;
				}
			}
		}
	}
}