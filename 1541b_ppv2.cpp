/**
 * @file 1541b_ppv2.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Pleasant
 * Pairs(https://codeforces.com/problemset/problem/1541/B)
 * @version 0.1
 * @date 2025-01-07
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
    ll t, n, i, j, res;
    vector<pair<ll, ll>> a;

    cin >> t;
    while (t--) {
        cin >> n, i = res = 0;
        a.resize(n);
        for (auto &ai : a) {
            cin >> ai.first;
            ai.second = ++i;
        }
        sort(a.begin(), a.end());
        for (i = 0, j = 0; i < n; i++)
            for (j = i + 1; j < n; j++) {
                if (a[i].first * a[j].first > 2 * n)
                    break;
                res += a[i].second + a[j].second == a[i].first * a[j].first;
            }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}