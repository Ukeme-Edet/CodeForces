/**
 * @file 1780b_gcdp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem GCD
 * Partition(https://codeforces.com/problemset/problem/1780/B)
 * @version 0.1
 * @date 2025-01-11
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
    ll t, n, res, ai, i;
    vector<ll> psa;

    cin >> t;
    while (t--) {
        cin >> n;
        psa.clear();
        psa.resize(n + 1, 0);
        for (i = 1; i <= n; i++) {
            cin >> ai;
            psa[i] = psa[i - 1] + ai;
        }
        res = 0;
        for (i = 1; i < n; i++)
            res = max(res, gcd(psa[i], psa[n] - psa[i]));
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}