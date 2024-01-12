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
	short t, n, c;
	string s;
	char res[2];
	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		c = 0;
		for (int i = 0; i < n && c < 2; i++)
			s[i] % 2 ? res[c++] = s[i] : 0;
		c < 2 ? cout << "-1\n" : cout << res[0] << res[1] << '\n';
	}
	return (EXIT_SUCCESS);
}
