#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, i;
	int k;

	cin >> t;
	while (t--)
	{
		cin >> k;
		i = 1;
		while (k > (long long)i * i)
			i++;
		if (k > (long long)(i - 1) * (i - 1) + i)
			cout << i << ' ' << (long long)i * i - k + 1 << '\n';
		else
			cout << k - (long long)(i - 1) * (i - 1) << ' ' << i << '\n';
	}
	return (EXIT_SUCCESS);
}
