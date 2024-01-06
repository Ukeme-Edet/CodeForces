#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function of the program.
 *
 * @return int The exit status of the program.
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	long long a, b, nop;

	cin >> t;
	while (t--)
	{
		cin >> a >> b;
		nop = 0;
		if (a > b)
			swap(a, b);
		while (a < b)
		{
			a *= 2;
			nop++;
		}
		if (a != b)
			cout << "-1\n";
		else
			cout << (nop / 3) + ((nop % 3) / 2) + ((nop % 3) % 2) << "\n";
	}
	return (EXIT_SUCCESS);
}
