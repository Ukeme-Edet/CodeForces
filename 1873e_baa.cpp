/**
 * @file 1873e_baa.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Building an
 * Aquarium(https://codeforces.com/problemset/problem/1873/E)
 * @version 0.1
 * @date 2024-10-17
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll vol_h2o(vector<ll> aq, ll h) {
    ll res = 0;

    for (const auto ai : aq)
        res += max(0ll, h - ai);
    return res;
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t, n, x, w, l, r, m, res;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n >> x;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        l = 0, r = 2000000000, res = 0;
        while (l <= r) {
            m = l + (r - l) / 2;
            w = vol_h2o(a, m);
            if (w > x)
                r = m - 1;
            else
                res = max(res, m), l = m + 1;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}