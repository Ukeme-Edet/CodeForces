/**
 * @file 1366b_shuffle.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem
 * Shuffle(https://codeforces.com/problemset/problem/1366/B)
 * @version 0.1
 * @date 2025-01-06
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
    ll t, n, x, m, l, r, mas, mis;

    cin >> t;
    while (t--) {
        cin >> n >> x >> m;
        mas = mis = x;
        while (m--) {
            cin >> l >> r;
            if (max(l, mis) <= min(r, mas))
                mis = min(mis, l), mas = max(mas, r);
        }
        cout << mas - mis + 1 << '\n';
    }
    return (EXIT_SUCCESS);
}