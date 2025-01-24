/**
 * @file 1511c_yacd.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Yet Another Card
 * Deck(https://codeforces.com/problemset/problem/1511/C)
 * @version 0.1
 * @date 2025-01-24
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
    ll n, q, i;
    vector<ll> a, t;
    map<ll, ll> m;

    cin >> n >> q;
    a.resize(n), t.resize(q);
    for (auto &ai : a)
        cin >> ai;
    for (auto &ti : t)
        cin >> ti;
    for (i = n - 1; i >= 0; i--)
        m[a[i]] = i;
    for (i = 0; i < q; i++) {
        cout << m[t[i]] + 1 << ' ';
        for (auto &mi : m)
            if (mi.second < m[t[i]])
                mi.second++;
        m[t[i]] = 0;
    }
    return (EXIT_SUCCESS);
}