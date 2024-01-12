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
	int rgb[3];

	cin >> t;
	while (t--)
	{
		cin >> rgb[0] >> rgb[1] >> rgb[2];
		sort(rgb, rgb + 3);
		rgb[2] - rgb[1] - rgb[0] > 1 ? cout << "No\n" : cout << "Yes\n";
	}
	return (EXIT_SUCCESS);
}
