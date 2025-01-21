/**
 * @file 1487b_cc.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Cat Cycle
 * (https://codeforces.com/problemset/problem/1487/B)
 * @version 0.1
 * @date 2025-01-21
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
    ll t, n, k;

    cin >> t;
    while (t--) {
        cin >> n >> k;
        k--;
        cout << (k + (k / (n / 2)) * (n % 2)) % n + 1 << '\n';
    }
    return (EXIT_SUCCESS);
}