/**
 * @file 26a_ap.cpp
 * @author Ukeme Edet
 * @brief This is the solution to codeforces problem 26A
 * @version 0.1
 * @date 2024-01-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <bits/stdc++.h>

using namespace std;

/**
 * @brief Get the primes object
 *
 * @param n
 * @param primes
 */
void get_primes(short n, vector<short> &primes)
{
	short i, j;
	primes.resize(n / 2 + 1, 1);
	primes[0] = primes[1] = 0;
	for (i = 2; i * i <= n; i++)
		if (primes[i])
			for (j = i * i; j <= n / 2; j += i)
				primes[j] = 0;
}

/**
 * @brief main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short n, i, j, ans = 0, c;
	vector<short> primes;

	cin >> n;
	get_primes(n, primes);
	for (i = 6; i <= n; i++)
	{
		c = 0;
		for (j = 0; j < primes.size() && c < 3; j++)
			if (primes[j] && i % j == 0)
				c++;
		if (c == 2)
			ans++;
	}
	cout << ans << '\n';
	return (EXIT_SUCCESS);
}
