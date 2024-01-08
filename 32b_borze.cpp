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
	string s;
	int i = 0;

	cin >> s;
	while (i < s.length())
	{
		if (s[i] == '.')
		{
			cout << 0;
			i++;
		}
		else if (s[i] == '-' && s[i + 1] == '.')
		{
			cout << 1;
			i += 2;
		}
		else if (s[i] == '-' && s[i + 1] == '-')
		{
			cout << 2;
			i += 2;
		}
	}
	cout << '\n';
	return (EXIT_SUCCESS);
}
