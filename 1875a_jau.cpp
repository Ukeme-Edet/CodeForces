/**
 * @file 1875a_jau.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Jellyfish and
 * Undertale(https://codeforces.com/problemset/problem/1875/A)
 * @version 0.1
 * @date 2025-02-06
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
    ll t, a, b, n;
    vector<ll> x;

    cin >> t;
    while (t--) {
        cin >> a >> b >> n;
        x.resize(n);
        for (auto &ai : x) {
            cin >> ai;
            if (ai >= a)
                ai = a - 1;
        }
        cout << accumulate(x.begin(), x.end(), 0ll) + b << '\n';
    }
    return (EXIT_SUCCESS);
}