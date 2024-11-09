/**
 * @file 1842b_tab.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Tenzing and
 * Books(https://codeforces.com/problemset/problem/1842/B)
 * @version 0.1
 * @date 2024-11-09
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
    ll t, n, i, u, cv, x, xc;
    vector<ll> a, b, c;

    cin >> t;
    while (t--) {
        cin >> n >> x;
        a.resize(n), b.resize(n), c.resize(n);
        for (auto &ai : a)
            cin >> ai;
        for (auto &bi : b)
            cin >> bi;
        for (auto &ci : c)
            cin >> ci;
        u = 0;
        auto s = {&a, &b, &c};
        for (const auto &si : s) {
            for (i = 0; i < n; i++) {
                cv = (*si)[i], xc = x;
                while (cv && xc) {
                    if ((cv & 1) > (xc & 1))
                        break;
                    cv >>= 1, xc >>= 1;
                }
                if (cv)
                    break;
                u |= (*si)[i];
            }
        }
        cout << (u == x ? "YES" : "NO") << '\n';
    }
    return (EXIT_SUCCESS);
}