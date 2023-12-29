#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function :)
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n;
	bool found;
	long long total = 0, tmp;
	cin >> t;
	while (t--)
	{
		found = false;
		total = 0;
		map<long long, bool> m;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> tmp;
			m[total] = true;
			i % 2 ? total -= tmp : total += tmp;
			if (m[total])
				found = true;
		}
		found || m[total] ? cout << "YES\n" : cout << "NO\n";
	}
}
