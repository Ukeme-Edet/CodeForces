#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	string a, b;
	cin >> t;
	while (t--)
	{
		cin >> a >> b;
		if (a.size() > b.size())
		{
			string temp = a;
			a = b, b = temp;
		}
		int ans = 0;
		for (int i = 0; i < a.size(); i++)
		{
			for (int j = 1; j <= a.size() - i; j++)
				if (b.find(a.substr(i, j)) != string::npos)
					ans = max(ans, j);
		}
		cout << a.size() + b.size() - 2 * ans << "\n";
	}
}
