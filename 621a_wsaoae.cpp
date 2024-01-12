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
	int n, temp, c = 0;
	long long sum = 0;

	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		if (temp % 2 == 0)
			sum += temp;
		else
			v[c++] = temp;
	}
	sort(v.rbegin(), v.rend());
	for (int i = 0; i < c - 1; i += 2)
		sum += v[i] + v[i + 1];
	cout << sum << '\n';
	return (EXIT_SUCCESS);
}
