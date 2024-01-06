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
	short t;
	int a, b;

	cin >> t;
	while (t--)
	{
		cin >> a >> b;
		(a & 1) ^ (b & 1) ? cout << "Alice\n" : cout << "Bob\n";
	}
	return (EXIT_SUCCESS);
}
