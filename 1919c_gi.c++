/**
 * @file 1919c_gi.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Grouping
 * Increases(https://codeforces.com/contest/1919/problem/C)
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
    ll t, n, ai, s1, s2, i, res;

    cin >> t;
    while (t--) {
        cin >> n, s1 = s2 = LLONG_MAX, res = 0;
        for (i = 0; i < n; i++) {
            cin >> ai;
            if (ai <= s1 && ai <= s2)
                s1 > s2 ? s2 = ai : s1 = ai;
            else if (ai <= s1)
                s1 = ai;
            else if (ai <= s2)
                s2 = ai;
            else
                res++, s1 < s2 ? s1 = ai : s2 = ai;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}