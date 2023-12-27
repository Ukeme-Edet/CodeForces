#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	unordered_map<string, int> db;
	string name;
	cin >> n;
	while (n--)
	{
		cin >> name;
		if (db.find(name) == db.end())
		{
			cout << "OK\n";
			db[name] = 1;
		}
		else
		{
			cout << name << db[name] << "\n";
			db[name]++;
		}
	}
}
