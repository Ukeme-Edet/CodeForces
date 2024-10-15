/**
 * @file 2025c_ng.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem New
 * Game(https://codeforces.com/contest/2025/problem/C)
 * @version 0.1
 * @date 2024-10-15
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
    ll t, n, k, ai, i, res, pc, cs, l, r;
    vector<ll> cmv, v;
    map<ll, ll> cm;

    cin >> t;
    while (t--) {
        cin >> n >> k, res = cs = pc = 0;
        cm.clear(), cmv.clear(), v.clear();
        for (i = 0; i < n; i++) {
            cin >> ai;
            cm[ai]++;
        }
        for (const auto cmi : cm)
            cmv.push_back(cmi.second), v.push_back(cmi.first);
        l = r = 0;
        while (r < cmv.size()) {
            if (v[r] - pc > 1)
                cs = 0, l = r;
            cs += cmv[r];
            if (r - l + 1 > k)
                cs -= cmv[l++];
            pc = v[r];
            r++;
            res = max(res, cs);
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}