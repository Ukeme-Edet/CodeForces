#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n, a;
	int x, min_m, max_m, i;

	cin >> t;
	while (t--)
	{
		map<int, bool> m;

		cin >> n;
		max_m = INT_MIN;
		min_m = INT_MAX;
		for (i = 0; i < n; i++)
		{
			cin >> a >> x;
			if (a == 1)
				max_m = max(max_m, x);
			else if (a == 2)
				min_m = min(min_m, x);
			else
				m[x] = true;
		}
		if (max_m > min_m)
		{
			cout << 0 << '\n';
			continue;
		}
		i = 0;
		for (auto &it : m)
			if (it.first >= max_m && it.first <= min_m)
				i++;
		cout << min_m - max_m - i + 1 << '\n';
	}
	return (EXIT_SUCCESS);
}
