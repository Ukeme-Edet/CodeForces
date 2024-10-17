/**
 * @file 1846e1_ras.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Rudolf and Snowflakes (simple
 * version)(https://codeforces.com/problemset/problem/1846/E1)
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
    ll t, n, i = 2, ov, cv;
    map<ll, bool> sm;

    for (i = 2; (pow(i, 3) - 1) / (i - 1) <= 1000000; i++) {
        ov = pow(i, 3), cv = (pow(i, 3) - 1) / (i - 1);
        while (cv <= 1000000) {
            sm[cv] = 1;
            cv += ov;
            ov *= i;
        }
    }
    cin >> t;
    while (t--) {
        cin >> n;
        cout << (sm[n] ? "YES\n" : "NO\n");
    }
    return (EXIT_SUCCESS);
}