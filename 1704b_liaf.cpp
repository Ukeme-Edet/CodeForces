/**
 * @file 1704b_liaf.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Luke is a
 * Foodie(https://codeforces.com/problemset/problem/1704/B)
 * @version 0.1
 * @date 2024-12-01
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
    ll t, n, x, res, mi, ma, i, ai;

    cin >> t;
    while (t--) {
        cin >> n >> x, res = 0;
        mi = LLONG_MAX, ma = LLONG_MIN;
        for (i = 0; i < n; i++) {
            cin >> ai;
            mi = min(mi, ai), ma = max(ma, ai);
            if (ma - mi > x * 2)
                ma = mi = ai, res++;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}