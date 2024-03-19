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
	int oc, zc;
	string s;

	cin >> t;
next:
	while (t--)
	{
		cin >> s;
		zc = count(s.begin(), s.end(), '0'), oc = count(s.begin(), s.end(), '1');
		for (char &c : s)
		{
			if (c == '1')
			{
				if (zc == 0)
				{
					cout << oc << '\n';
					goto next;
				}
				zc--;
			}
			else
			{
				if (oc == 0)
				{
					cout << zc << '\n';
					goto next;
				}
				oc--;
			}
		}
		cout << 0 << '\n';
	}
	return (EXIT_SUCCESS);
}
