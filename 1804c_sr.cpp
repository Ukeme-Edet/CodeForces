/**
 * @file 1804c_sr.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Ski
 * Resort(https://codeforces.com/problemset/problem/1840/C)
 * @version 0.1
 * @date 2024-10-16
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
    ll t, n, k, q, ai, res, tr, i, nt;

    cin >> t;
    while (t--) {
        cin >> n >> k >> q, res = tr = 0;
        for (i = 0; i < n; i++) {
            cin >> ai;
            if (ai > q) {
                nt = tr - k + 1;
                res += nt > 0 ? max(0ll, nt * (nt + 1) / 2) : 0;
                tr = 0;
                continue;
            }
            tr++;
        }
        nt = tr - k + 1;
        res += nt > 0 ? max(0ll, nt * (nt + 1) / 2) : 0;
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}