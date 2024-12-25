/**
 * @file 1470a_sbp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Strange Birthday
 * Party(https://codeforces.com/problemset/problem/1470/A)
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
    ll t, n, m, li, res;
    vector<ll> pb, k, c;

    cin >> t;
    while (t--) {
        cin >> n >> m;
        k.resize(n), c.resize(m);
        for (auto &ki : k)
            cin >> ki;
        for (auto &ci : c)
            cin >> ci;
        sort(k.rbegin(), k.rend());
        li = res = 0;
        for (const auto &ki : k)
            res += li < ki ? c[li++] : c[ki - 1];
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}