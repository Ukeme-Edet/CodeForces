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
	short n, m, i;
	string name, ip;
	map<string, string> db;

	cin >> n >> m;
	for (i = 0; i < n; i++)
	{
		cin >> name >> ip;
		db[ip] = name;
	}
	for (i = 0; i < m; i++)
	{
		cin >> name >> ip;
		cout << name << ' ' << ip << " #" << db[ip.substr(0, ip.size() - 1)] << '\n';
	}
	return (EXIT_SUCCESS);
}
