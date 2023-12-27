#include <bits/stdc++.h>

using namespace std;

/**
 * @brief A function to find the maximum digit in a number.
 *
 * @param a  The number whose maximum digit is to be found.
 * @return unsigned long long
 */
unsigned long long max_d(unsigned long long a)
{
	unsigned long long maxd = 0;

	while (a > 0)
	{
		if (a % 10 > maxd)
			maxd = a % 10;
		a /= 10;
	}
	return maxd;
}

/**
 * @brief A function to find the minimum digit in a number.
 *
 * @param a  The number whose minimum digit is to be found.
 * @return unsigned long long
 */
unsigned long long min_d(unsigned long long a)
{
	unsigned long long mind = 9;

	while (a > 0)
	{
		if (a % 10 < mind)
			mind = a % 10;
		a /= 10;
	}
	return mind;
}

/**
 * @brief The main function
 *
 * @return int
 */
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	unsigned short int t;
	scanf("%hu", &t);
	unsigned long long a, k;

	while (t--)
	{
		scanf("%llu %llu", &a, &k);
		k--;
		while (k-- && min_d(a) != 0)
			a = a + max_d(a) * min_d(a);
		printf("%llu\n", a);
	}
}
