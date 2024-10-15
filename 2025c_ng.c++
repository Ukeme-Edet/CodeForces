/**
 * @file 2025c_ng.c++
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
    ll t, n, k, ai, i, cs, res;
    queue<ll> kq;
    map<ll, ll> km;

    cin >> t;
    while (t--) {
        cin >> n >> k, km.clear(), queue<ll>().swap(kq);
        for (i = 0; i < n; i++) {
            cin >> ai;
            km[ai]++;
        }
        cs = res = 0;
        for (const auto kmi : km) {
            kq.size() && kmi.first - kq.back() > 1 ? cs = 0,
                                                     queue<ll>().swap(kq)
                                                   : void();
            cs += kmi.second;
            kq.push(kmi.first);
            if (kq.size() > k) {
                cs -= km[kq.front()];
                kq.pop();
            }
            res = max(res, cs);
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}