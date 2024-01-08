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
	short t, n, nc, ans1;
	int temp;

	cin >> t;
	while (t--)
	{
		ans1 = 1, nc = 0;
		cin >> n;
		for (short i = 0; i < n; i++)
		{
			cin >> temp;
			temp == 0 ? ans1 = 0 : 0;
			temp < 0 ? nc++ : 0;
		}
		(!ans1 || nc % 2) ? cout << 0 << '\n' : cout << "1\n1 0\n";
	}
	return (EXIT_SUCCESS);
}
