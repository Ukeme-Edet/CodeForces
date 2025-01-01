/**
 * @file 1917b_efoslv2.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Erase First or Second
 * Letter(https://codeforces.com/problemset/problem/1917/B)
 * @version 0.1
 * @date 2025-01-01
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
    ll t, n, i, res, seen[26];
    string s;

    cin >> t;
    while (t--) {
        cin >> n >> s, res = 0;
        memset(seen, 0, sizeof(seen));
        for (i = 0; i < n; i++) {
            if (!seen[s[i] - 'a']) {
                seen[s[i] - 'a'] = 1;
                res += n - i;
            }
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}