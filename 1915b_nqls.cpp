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
	vector<string> v(3);
	cin >> t;
	while (t--)
	{
		cin >> v[0] >> v[1] >> v[2];
		for (short i = 0; i < 3; i++)
			if (v[i].find("?") != string::npos)
				v[i].find("A") == string::npos ? cout << "A\n" : (v[i].find("B") == string::npos ? cout << "B\n" : cout << "C\n");
	}
	return 0;
}
