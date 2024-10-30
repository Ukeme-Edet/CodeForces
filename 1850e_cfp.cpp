/**
 * @file 1850e_cfp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Cardboard for
 * Pictures(https://codeforces.com/problemset/problem/1850/E)
 * @version 0.1
 * @date 2024-10-30
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
    ll t, n, c, l, r, m, cc, res;
    vector<ll> s;

    cin >> t;
    while (t--) {
        cin >> n >> c;
        s.resize(n);
        for (auto &si : s)
            cin >> si;
        l = 0, r = pow(1000000000000000000 / n, .5);
        while (l <= r) {
            m = l + (r - l) / 2;
            cc = 0;
            for (const auto &si : s)
                cc += (si + m + m) * (si + m + m);
            if (cc < c)
                l = m + 1;
            else if (cc > c)
                r = m - 1;
            else {
                res = m;
                break;
            }
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}