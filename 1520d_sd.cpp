/**
 * @file 1520d_sd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Same
 * Differences(https://codeforces.com/problemset/problem/1520/D)
 * @version 0.1
 * @date 2025-01-13
 *
 * @copyright Copyright (c) 2025
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
    ll t, n, i, j, x, res;
    map<ll, ll> dm;

    cin >> t;
    while (t--) {
        cin >> n;
        i = 1, res = 0, dm.clear();
        for (j = 0; j < n; j++) {
            cin >> x;
            dm[x - i++]++;
        }
        for (const auto &[k, v] : dm)
            res += (v * (v - 1)) / 2;
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}