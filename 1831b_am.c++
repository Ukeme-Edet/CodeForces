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
    ll t, n, i, tv, pv, fm1[400001] = {0}, fm2[400001] = {0}, res, tres;

    cin >> t;
    while (t--) {
        cin >> n, res = tres = 0, pv = 0;
        for (i = 0; i < n; i++) {
            cin >> tv;
            if (pv == tv)
                tres++;
            else {
                fm1[pv] = max(fm1[pv], tres);
                tres = 1;
            }
            pv = tv;
        }
        fm1[pv] = max(fm1[pv], tres);
        tres = 0, pv = 0;
        for (i = 0; i < n; i++) {
            cin >> tv;
            if (pv == tv)
                tres++;
            else {
                fm2[pv] = max(fm2[pv], tres);
                tres = 1;
            }
            pv = tv;
        }
        fm2[pv] = max(fm2[pv], tres);
        for (i = 1; i <= 2 * n; i++) {
            res = max(res, fm1[i] + fm2[i]);
            fm1[i] = fm2[i] = 0;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}