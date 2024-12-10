/**
 * @file 1830a_ccdt.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Copil Copac Draws
 * Trees(https://codeforces.com/contest/1830/problem/A)
 * @version 0.1
 * @date 2024-12-10
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

#define ll long long

using namespace std;

void scan(ll u, ll v, vector<vector<ll>> &am, vector<ll> &ac,
          map<pair<ll, ll>, ll> &idx, unordered_map<ll, ll> &dp) {
    for (const auto &x : am[v]) {
        if (x == u)
            continue;
        if (idx[{v, x}] >= ac[v])
            dp[x] = dp[v];
        else
            dp[x] = dp[v] + 1;
        ac[x] = idx[{v, x}];
        scan(v, x, am, ac, idx, dp);
    }
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t, n, u, v, i, res;
    vector<ll> ac;
    vector<vector<ll>> am;
    map<pair<ll, ll>, ll> idx;
    unordered_map<ll, ll> dp;

    cin >> t;
    while (t--) {
        cin >> n, am.clear(), idx.clear(), ac.resize(n + 1), dp.clear();
        ac[1] = 0, dp[1] = 1, am.resize(n + 1);
        for (i = 0; i < n - 1; i++) {
            cin >> u >> v;
            am[u].push_back(v), am[v].push_back(u);
            idx[{u, v}] = idx[{v, u}] = i;
        }
        scan(0, 1, am, ac, idx, dp);
        res = 0;
        for (const auto &x : dp)
            res = max(res, x.second);
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}