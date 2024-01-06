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
	int n, temp, res;

	cin >> t;
	while (t--)
	{
		queue<int> q1, q2;

		cin >> n;
		res = 0;
		q1.push(INT_MAX);
		q2.push(INT_MAX);
		for (int i = 0; i < n; ++i)
		{
			cin >> temp;
			if (temp <= q1.back() && temp <= q2.back())
			{
				if (q1.back() <= q2.back())
					q1.push(temp);
				else
					q2.push(temp);
			}
			else if (temp <= q1.back())
				q1.push(temp);
			else if (temp <= q2.back())
				q2.push(temp);
			else
			{
				if (q1.back() <= q2.back())
					q1.push(temp);
				else
					q2.push(temp);
				res++;
			}
		}
		cout << res << '\n';
	}
	return (EXIT_SUCCESS);
}
