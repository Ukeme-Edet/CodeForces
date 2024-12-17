/**
 * @file 1671c_dv.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Dolce
 * Vita(https://codeforces.com/problemset/problem/1671/C)
 * @version 0.1
 * @date 2024-12-17
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
    ll t, n, x, i, res, ps;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n >> x, res = 0;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        sort(a.begin(), a.end());
        for (i = 1, ps = a[0]; i <= n && ps <= x; i++) {
            res += ((x - ps) / i) + 1;
            ps += a[i];
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}