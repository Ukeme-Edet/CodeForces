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
	short n, m, c, mc = 0, cc = 0;

	cin >> n;
	while (n--)
	{
		cin >> m >> c;
		if (m > c)
			mc++;
		else if (c > m)
			cc++;
	}
	mc > cc ? cout << "Mishka\n" : cc > mc ? cout << "Chris\n"
										   : cout << "Friendship is magic!^^\n";
}
