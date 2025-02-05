/**
 * @file 1418a_bt.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Buying
 * Torches(https://codeforces.com/problemset/problem/1418/A)
 * @version 0.1
 * @date 2024-09-02
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long t, x, y, k, ans;

    cin >> t;
    while (t--) {
        cin >> x >> y >> k;
        ans = (y * k + k - 1) / (x - 1) + k;
        cout << ((y * k + k - 1) % (x - 1) ? ans + 1 : ans) << '\n';
    }
    return (EXIT_SUCCESS);
}