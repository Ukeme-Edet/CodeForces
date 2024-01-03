#include <bits/stdc++.h>

using namespace std;

/**
 * @brief This is the main function
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, ans, ci;
	string s;
	char c;

	cin >> t;
	while (t--)
	{
		cin >> n >> c >> s;
		ans = INT_MIN;
		for (int i = s.find(c, 0); i != string::npos; ci != string::npos ? i = s.find(c, ci + 1) : i = ci)
		{
			ci = s.find('g', i);
			if (ci != string::npos)
			{
				ans = max(ans, ci - i);
			}
			else
			{
				ans = max(ans, (int)(s.find('g') + n - i));
			}
		}
		cout << ans << '\n';
	}
	return (0);
}
