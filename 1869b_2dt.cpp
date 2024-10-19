/**
 * @file 1869b_2dt.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem 2D
 * Traveling(https://codeforces.com/problemset/problem/1869/B)
 * @version 0.1
 * @date 2024-10-19
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
    ll t, n, k, a, b, md1, md2, i;
    vector<pair<ll, ll>> v;

    cin >> t;
    while (t--) {
        cin >> n >> k >> a >> b;
        v.resize(n);
        for (auto &vi : v)
            cin >> vi.first >> vi.second;
        md1 = md2 = LLONG_MAX / 2;
        for (i = 0; i < k; i++) {
            md1 = min(md1, abs(v[i].first - v[a - 1].first) +
                               abs(v[i].second - v[a - 1].second));
            md2 = min(md2, abs(v[i].first - v[b - 1].first) +
                               abs(v[i].second - v[b - 1].second));
        }
        cout << min(md1 + md2, abs(v[a - 1].first - v[b - 1].first) +
                                   abs(v[a - 1].second - v[b - 1].second))
             << '\n';
    }
    return (EXIT_SUCCESS);
}