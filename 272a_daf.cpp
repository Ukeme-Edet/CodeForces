#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	unsigned short int hands, temp, n, hand, ways = 0;
	hands = 0;
	cin >> n;
	for (unsigned short int i = 0; i < n; i++)
	{
		cin >> temp;
		hands += temp;
	}
	hand = 1;
	while (hand < 6)
	{
		if ((hands + hand) % (n + 1) != 1)
			ways++;
		hand++;
	}
	cout << ways << "\n";
}
