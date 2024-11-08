/**
 * @file 1790d_matryoshkas.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem
 * Matryoshkas(https://codeforces.com/problemset/problem/1790/D)
 * @version 0.1
 * @date 2024-11-08
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
    ll t, n, ai, i, res;
    set<ll> ds;
    map<ll, ll> dm;

    cin >> t;
    while (t--) {
        cin >> n;
        ds.clear(), dm.clear();
        for (i = 0; i < n; i++) {
            cin >> ai;
            ds.insert(ai);
            dm[ai]++;
        }
        res = 0;
        for (const auto &dsi : ds) {
            if (dm[dsi + 1] < dm[dsi])
                res += dm[dsi] - dm[dsi + 1];
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}