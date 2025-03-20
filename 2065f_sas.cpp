/**
 * @file 2065f_sas.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Skibidus and
 * Slay(https://codeforces.com/contest/2065/problem/F)
 * @version 0.1
 * @date 2025-03-19
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
    ll t, n, u, v, i, j;
    vector<ll> a;
    vector<char> res;
    vector<vector<ll>> adj;
    map<ll, ll> fm;

    cin >> t;
    while (t--) {
        cin >> n;
        adj = {}, res = {};
        adj.resize(n + 1), res.resize(n, '0'), a.resize(n);
        for (i = 0; i < n; i++)
            cin >> a[i];
        for (i = 0; i < n - 1; i++) {
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        for (i = 1; i <= n; i++) {
            fm = {};
            for (j = 0; j < adj[i].size(); j++)
                fm[a[adj[i][j] - 1]]++;
            fm[a[i - 1]]++;
            for (const auto &[k, v] : fm)
                if (v > 1)
                    res[k - 1] = '1';
        }
        for (i = 0; i < res.size(); i++)
            cout << res[i];
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}