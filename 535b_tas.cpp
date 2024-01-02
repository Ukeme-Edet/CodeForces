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
	int n, ans = 0, b = 1;
	map<int, int> lm = {{4, 1}, {7, 2}};

	cin >> n;
	while (n)
	{
		ans += lm[n % 10] * b;
		b *= 2;
		n /= 10;
	}
	cout << ans << '\n';
	return (0);
}