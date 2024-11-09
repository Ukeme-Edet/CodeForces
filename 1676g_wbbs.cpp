/**
 * @file 1676g_wbbs.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem White-Black Balanced
 * Subtrees(https://codeforces.com/problemset/problem/1676/G)
 * @version 0.1
 * @date 2024-11-09
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
    ll t, n, i, res;
    string s;
    vector<ll> a;
    vector<pair<ll, ll>> cc;
    map<ll, bool> d;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n - 1), cc.clear();
        d.clear(), cc.resize(n + 1);
        for (auto &ai : a)
            cin >> ai;
        cin >> s;
        for (i = n - 2; i >= 0; i--) {
            if (d[i + 2])
                continue;
            d[i + 2] = 1;
            s[i + 1] == 'W' ? cc[i + 2].first++ : cc[i + 2].second++;
            cc[a[i]].first += cc[i + 2].first;
            cc[a[i]].second += cc[i + 2].second;
        }
        s[0] == 'W' ? cc[1].first++ : cc[1].second++;
        res = 0;
        for (i = 1; i <= n; i++)
            res += cc[i].first == cc[i].second;
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}