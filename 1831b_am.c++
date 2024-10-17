/**
 * @file 1831b_am.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Array
 * merging(https://codeforces.com/problemset/problem/1831/B)
 * @version 0.1
 * @date 2024-10-17
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
    ll t, n, i, tv, fm[400001], res;

    cin >> t;
    while (t--) {
        cin >> n, memset(fm, 0, sizeof(ll) * 400001), res = 0;
        for (i = 0; i < 2 * n; i++) {
            cin >> tv;
            fm[tv]++;
        }
        for (i = 1; i <= 2 * n; i++)
            res = max(res, fm[i]);
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}