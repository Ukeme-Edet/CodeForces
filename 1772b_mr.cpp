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
	short a[2][2];

	cin >> t;
	while (t--)
	{
		cin >> a[0][0] >> a[0][1] >> a[1][0] >> a[1][1];
		((a[0][0] < a[0][1] && a[1][0] > a[1][1]) || (a[0][0] > a[0][1] && a[1][0] < a[1][1]) || (a[0][0] < a[1][0] && a[0][1] > a[1][1]) || (a[0][0] > a[1][0] && a[0][1] < a[1][1])) ? cout << "NO\n" : cout << "YES\n";
	}
	return (EXIT_SUCCESS);
}
