/**
 * @file 2037a_twice.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem
 * Twice(https://codeforces.com/contest/2037/problem/A)
 * @version 0.1
 * @date 2024-11-17
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
    ll t, n, ai, fm[21] = {0}, i, res;

    cin >> t;
    while (t--) {
        cin >> n, res = 0;
        for (i = 0; i < n; i++) {
            cin >> ai;
            fm[ai]++;
        }
        for (i = 0; i <= 20; i++) {
            res += fm[i] / 2;
            fm[i] = 0;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}