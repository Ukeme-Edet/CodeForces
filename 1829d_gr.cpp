#include <bits/stdc++.h>

using namespace std;

/**
 * @brief find_pile - find if there is a pile of stones that can be divided into two piles such that one is twice the other
 *
 * @param n The number of stones in the pile
 * @param m The target size
 * @param hm A hashmap to store the results of the subproblems
 * @return true
 * @return false
 */
bool find_pile(int n, int m, map<int, bool> &hm)
{
	if (hm.find(n) != hm.end())
		return (hm[n]);
	if (n == m)
		return (true);
	if (n < m)
	{
		hm[n] = false;
		return (false);
	}
	if (!(n % 3))
	{
		if (hm.find(n / 3) == hm.end())
			hm[n / 3] = find_pile(n / 3, m, hm);
		if (hm.find((n / 3) * 2) == hm.end())
			hm[(n / 3) * 2] = find_pile((n / 3) * 2, m, hm);
		return (hm[n / 3] || hm[(n / 3) * 2]);
	}
	hm[n] = false;
	return (false);
}

/**
 * @brief The main function :)
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t;
	int n, m;

	cin >> t;
	while (t--)
	{
		map<int, bool> hm;

		cin >> n >> m;
		find_pile(n, m, hm) ? cout << "YES\n" : cout << "NO\n";
	}
	return (0);
}