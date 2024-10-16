/**
 * @file 1891b_dv.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Deja
 * Vu(https://codeforces.com/problemset/problem/1891/B)
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
    ll t, n, q, le, i;
    vector<ll> a, x;

    cin >> t;
    while (t--) {
        cin >> n >> q;
        a.resize(n), x.resize(q);
        for (auto &ai : a)
            cin >> ai;
        for (auto &xi : x)
            cin >> xi;
        le = LLONG_MAX;
        for (const auto xi : x) {
            if (xi < le) {
                le = xi;
                for (auto &ai : a) {
                    for (i = 0; i < xi; i++)
                        if (ai & (1 << i))
                            break;
                    if (i == xi)
                        ai |= (1 << (xi - 1));
                }
            }
        }
        for (const auto ai : a)
            cout << ai << ' ';
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}