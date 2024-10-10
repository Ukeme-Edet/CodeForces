/**
 * @file 1899b_250ttot.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 250 Thousand Tons of
 * TNT(https://codeforces.com/problemset/problem/1899/B)
 * @version 0.1
 * @date 2024-10-10
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

#define ll long long

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t, n, i, j, res, ma, mi;
    vector<ll> a, aps;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n), aps.resize(n + 1);
        aps[0] = res = 0;
        for (auto &ai : a)
            cin >> ai;
        for (i = 1; i <= n; i++)
            aps[i] = aps[i - 1] + a[i - 1];
        for (i = 1; i <= n / 2; i++)
            if (!(n % i)) {
                ma = 0, mi = LLONG_MAX;
                for (j = 0; j + i <= n; j += i)
                    mi = min(mi, aps[j + i] - aps[j]),
                    ma = max(ma, aps[j + i] - aps[j]);
                res = max(ma - mi, res);
            }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}