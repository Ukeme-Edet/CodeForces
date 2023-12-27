#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short int t;
	unsigned int n, k, l, r;
	long long line_value;
	string line;
	cin >> t;
	while (t--)
	{
		line_value = 0;
		cin >> n;
		cin >> line;
		vector<int> pu(n, 0);
		k = 0;
		for (unsigned int i = 0; i < n; i++)
		{
			if (line[i] == 'R')
			{
				line_value += n - i - 1;
				pu[i] = 2 * i - n + 1;
			}
			else
			{
				line_value += i;
				pu[i] = n - 2 * i - 1;
			}
		}
		sort(pu.rbegin(), pu.rend());
		for (unsigned int i = 0; i < n; i++)
		{
			if (pu[i] > 0)
				line_value += pu[i];
			cout << line_value << " ";
		}
		cout << "\n";
	}
}
