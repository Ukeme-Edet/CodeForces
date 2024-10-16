/**
 * @file 1857d_sv.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Strong
 * Vertices(https://codeforces.com/problemset/problem/1857/D)
 * @version 0.1
 * @date 2024-10-16
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
    ll t, n, i, nr;
    vector<ll> a, b;
    vector<pair<ll, ll>> sm;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n), b.resize(n), sm.resize(n);
        for (auto &ai : a)
            cin >> ai;
        for (auto &bi : b)
            cin >> bi;
        i = 0;
        for (auto &smi : sm)
            smi.first = a[i] - b[i], smi.second = ++i;
        sort(sm.begin(), sm.end());
        nr = sm.end() -
             lower_bound(sm.begin(), sm.end(), make_pair(sm[n - 1].first, -1ll));
        cout << nr << '\n';
        for (i = n - nr; i < n; i++)
            cout << sm[i].second << ' ';
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}