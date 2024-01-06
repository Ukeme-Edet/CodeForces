#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function of the program.
 *
 * @return int The exit status of the program.
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n;
	string s;

	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		cout << abs(count(s.begin(), s.end(), '-') - count(s.begin(), s.end(), '+')) << "\n";
	}
	return (EXIT_SUCCESS);
}
