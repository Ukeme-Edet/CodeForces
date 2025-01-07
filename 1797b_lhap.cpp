/**
 * @file 1797b_lhap.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Li Hua and
 * Pattern(https://codeforces.com/problemset/problem/1797/B)
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
    ll t, n, k, i, j, ch;
    vector<vector<ll>> a;

    cin >> t;
    while (t--) {
        cin >> n >> k, ch = 0;
        a.resize(n);
        for (auto &i : a) {
            i.resize(n);
            for (auto &j : i)
                cin >> j;
        }
        for (i = 0; i < n / 2; i++)
            for (j = 0; j < n; j++)
                ch += a[i][j] != a[n - i - 1][n - j - 1];
        if (n % 2)
            for (i = 0; i < n / 2; i++)
                ch += (a[n / 2][i] != a[n / 2][n - i - 1]);
        cout << (ch <= k && (k - ch) % 2 <= n % 2 ? "YES\n" : "NO\n");
    }
    return (EXIT_SUCCESS);
}