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
	int n;
	string s;
	cin >> t;
	unordered_map<char, int> cm = {{'a', 0}, {'b', 1}, {'c', 1}, {'d', 1}, {'e', 0}};
	while (t--)
	{
		cin >> n >> s;
		for (auto i = 0; i < n; i++)
		{
			cout << s[i];
			if ((!cm[s[i]] && (i < n - 2 && cm[s[i + 1]]) && !(i < n - 3 && cm[s[i + 2]])) || (cm[s[i]] && (i < n - 2 && cm[s[i + 1]])))
				cout << ".";
		}
		cout << "\n";
	}
	return 0;
}
