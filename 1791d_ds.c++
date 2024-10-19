/**
 * @file 1791d_ds.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Distinct
 * Split(https://codeforces.com/problemset/problem/1791/D)
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
    ll t, n, ldc[200001] = {0}, rdc[200001] = {0}, seen[26], i, res;
    string s;

    cin >> t;
    while (t--) {
        cin >> n >> s;
        memset(seen, 0, sizeof(seen));
        for (i = 1; i < n; i++) {
            ldc[i] = ldc[i - 1] + !seen[s[i - 1] - 'a'];
            seen[s[i - 1] - 'a'] = 1;
        }
        memset(seen, 0, sizeof(seen));
        for (i = n - 2; i >= 0; i--) {
            rdc[i] = rdc[i + 1] + !seen[s[i + 1] - 'a'];
            seen[s[i + 1] - 'a'] = 1;
        }
        res = 0;
        for (i = 0; i < n; i++) {
            res = max(res, ldc[i + 1] + rdc[i]);
            ldc[i + 1] = rdc[i] = 0;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}