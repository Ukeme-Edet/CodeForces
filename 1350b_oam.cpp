/**
 * @file 1350b_oam.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Orac and
 * Models(https://codeforces.com/problemset/problem/1350/B)
 * @version 0.1
 * @date 2025-03-06
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
    ll t, n, i, j;
    vector<ll> s, dp;
    unordered_map<ll, vector<ll>> fm;
    for (i = 1; i <= 100000; i++)
        for (j = i + i; j <= 100000; j += i)
            fm[j].push_back(i);

    cin >> t;
    while (t--) {
        cin >> n;
        dp.clear();
        s.resize(n), dp.resize(n + 1);
        for (auto &si : s)
            cin >> si;
        for (i = n; i > 0; i--)
            for (const auto &fmi : fm[i])
                if (s[i - 1] > s[fmi - 1])
                    dp[fmi] = max(dp[fmi], 1 + dp[i]);
        cout << *max_element(dp.begin(), dp.end()) + 1 << '\n';
    }
    return (EXIT_SUCCESS);
}