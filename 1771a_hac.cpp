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
	short t;
	int n, i;

	cin >> t;
	while (t--)
	{
		cin >> n;
		int a[n];
		for (i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		if (a[0] == a[n - 1])
			cout << (long long)n * (long long)(n - 1) << '\n';
		else
			cout << (long long)(upper_bound(a, a + n, a[0]) - a) * (long long)(n - (lower_bound(a, a + n, a[n - 1]) - a)) * 2ll << '\n';
	}
	return (EXIT_SUCCESS);
}
