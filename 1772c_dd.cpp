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
	short t, k, n, ne, e, d;
	cin >> t;
	while (t--)
	{
		cin >> k >> n;
		ne = 0, e = 1, d = 1;
		while (ne++ < k)
		{
			cout << e << " ";
			e += d;
			d++;
			if (d == n)
				d = 1;
		}
		cout << "\n";
	}
	return (EXIT_SUCCESS);
}
