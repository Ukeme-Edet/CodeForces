/**
 * @file 1808b_piac.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Playing in a
 * Casino(https://codeforces.com/problemset/problem/1808/B)
 * @version 0.1
 * @date 2024-10-17
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
    ll t, n, m, i, res;
    vector<vector<ll>> c;

    cin >> t;
    while (t--) {
        cin >> n >> m, res = 0;
        c.resize(m);
        for (auto &ci : c)
            ci.resize(n);
        for (i = 0; i < n * m; i++)
            cin >> c[i % m][i / m];
        for (auto &ci : c) {
            sort(ci.rbegin(), ci.rend());
            for (i = 0; i < n; i++)
                res += ci[i] * (n - i - i - 1);
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}