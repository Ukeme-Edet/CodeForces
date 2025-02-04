/**
 * @file 1447b_nb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Numbers
 * Box(https://codeforces.com/problemset/problem/1447/B)
 * @version 0.1
 * @date 2025-02-04
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
    ll t, n, m, res, nc, i, j;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n >> m, res = nc = 0, a.resize(n * m);
        for (auto &x : a) {
            cin >> x;
            nc ^= (x < 0);
            x = abs(x);
        }
        sort(a.begin(), a.end());
        cout << accumulate(a.begin(), a.end(), 0LL) - (nc ? a[0] : 0) * 2
             << '\n';
    }
    return (EXIT_SUCCESS);
}