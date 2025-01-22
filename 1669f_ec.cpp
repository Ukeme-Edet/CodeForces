/**
 * @file 1669f_ec.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Eating
 * Candies(https://codeforces.com/problemset/problem/1669/F)
 * @version 0.1
 * @date 2025-01-22
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
    ll t, n, l, r, res, ls, rs;
    vector<ll> w;

    cin >> t;
    while (t--) {
        cin >> n;
        w.resize(n);
        for (auto &wi : w)
            cin >> wi;
        l = res = ls = rs = 0, r = n - 1;
        while (l <= r) {
            if (ls <= rs) {
                ls += w[l];
                l++;
            } else {
                rs += w[r];
                r--;
            }
            if (ls == rs)
                res = l + n - r - 1;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}