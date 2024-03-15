/**
 * @file 1944b_exor.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Equal XOR(https://codeforces.com/contest/1944/problem/B)
 * @version 0.1
 * @date 2024-03-16
 *
 * @copyright Copyright (c) 2024
 *
 */

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
	int n, k, i, t1, t2;
	vector<int> a1, a2;

	cin >> t;
	while (t--)
	{
		cin >> n >> k;
		a1.resize(n);
		a2.resize(n);
		for (int &a1i : a1)
			cin >> a1i;
		for (int &a2i : a2)
			cin >> a2i;
		sort(a1.begin(), a1.end());
		sort(a2.begin(), a2.end());
		for (i = 1; i < n; i++)
			if (a1[i] == a1[i - 1])
			{
				t1 = a1[i];
				t2 = i;
				while (i - 2 > -1)
				{
					a1[i] = a1[i - 2];
					i--;
				}
				a1[0] = t1;
				a1[1] = t1;
				i = t2;
			}
		for (i = 1; i < n; i++)
			if (a2[i] == a2[i - 1])
			{
				t1 = a2[i];
				t2 = i;
				while (i - 2 > -1)
				{
					a2[i] = a2[i - 2];
					i--;
				}
				a2[0] = t1;
				a2[1] = t1;
				i = t2;
			}
		for (i = 0; i < k * 2; i++)
			cout << a1[i] << " ";
		cout << '\n';
		for (i = 0; i < k * 2; i++)
			cout << a2[i] << " ";
		cout << '\n';
	}
	return (EXIT_SUCCESS);
}
