/**
 * @file 1209g1_ib.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Into Blocks (easy
 * version)(https://codeforces.com/contest/1209/problem/G1)
 * @version 0.1
 * @date 2024-10-29
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
    ll n, q, i, res = 0, lim, mtr, ii;
    vector<ll> a;
    map<ll, ll> m;
    map<ll, pair<ll, ll>> mp;

    cin >> n >> q, i = 0;
    a.resize(n);
    for (auto &ai : a) {
        cin >> ai;
        if (m[ai])
            mp[ai].second = i;
        else
            mp[ai].first = i, mp[ai].second = i;
        m[ai]++, i++;
    }
    for (i = 0; i < n; i++) {
        ii = i, mtr = m[a[i]], lim = mp[a[i]].second;
        while (i < mp[a[lim]].second) {
            mtr = max(mtr, m[a[i]]);
            lim = max(lim, mp[a[i]].second);
            i++;
        }
        res += lim - ii - mtr + 1;
        i = lim;
    }
    cout << res << '\n';
    return (EXIT_SUCCESS);
}