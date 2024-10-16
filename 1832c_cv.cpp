/**
 * @file 1832c_cv.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Contrast
 * Value(https://codeforces.com/problemset/problem/1832/C)
 * @version 0.1
 * @date 2024-10-16
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
    ll t, n, ai, i, s, pv, res;

    cin >> t;
    while (t--) {
        cin >> n >> pv, res = s = 0;
        for (i = 1; i < n; i++) {
            cin >> ai;
            if (s == 0)
                ai != pv ? (s = ai > pv ? 1 : -1, res++) : 0;
            else if (s == 1 && ai < pv)
                res++, s = -1;
            else if (s == -1 && ai > pv)
                res++, s = 1;
            pv = ai;
        }
        cout << res + 1 << '\n';
    }
    return (EXIT_SUCCESS);
}