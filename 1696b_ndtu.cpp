/**
 * @file 1696b_ndtu.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem NIT Destroys the
 * Universe(https://codeforces.com/problemset/problem/1696/B)
 * @version 0.1
 * @date 2025-02-13
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
    ll t, n, res;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        res = 0;
        for (ll i = 0; i < n; i++) {
            if (a[i] != 0) {
                res++;
                while (i < n && a[i] != 0)
                    i++;
            }
        }
        cout << min(res, 2ll) << '\n';
    }
    return (EXIT_SUCCESS);
}