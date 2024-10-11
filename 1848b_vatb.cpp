/**
 * @file 1848b_vatb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Vika and the
 * Bridge(https://codeforces.com/problemset/problem/1848/B)
 * @version 0.1
 * @date 2024-10-11
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
    ll t, n, k, i, res, dist, tv, c;
    vector<ll> ms1, ms2;

    cin >> t;
    while (t--) {
        cin >> n >> k;
        vector<ll> li(k + 1, -1), ms1(k + 1, -1), ms2(k + 1, -1);
        res = LLONG_MAX;
        for (i = 0; i < n; i++) {
            cin >> c;
            dist = i - li[c] - 1;
            tv = ms1[c];
            ms1[c] = max(ms1[c], dist);
            ms2[c] = ms1[c] != tv ? max(tv, ms2[c]) : max(ms2[c], dist);
            li[c] = i;
        }
        for (i = 1; i <= k; i++) {
            if (ms1[i] == -1)
                continue;
            dist = n - li[i] - 1;
            tv = ms1[i];
            ms1[i] = max(ms1[i], dist);
            ms2[i] = ms1[i] != tv ? max(tv, ms2[i]) : max(ms2[i], dist);
            res = min(res, max(ms2[i], ms1[i] / 2));
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}