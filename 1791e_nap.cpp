/**
 * @file 1791e_nap.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Negatives and
 * Positives(https://codeforces.com/problemset/problem/1791/E)
 * @version 0.1
 * @date 2025-01-09
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
    ll t, n, i;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        sort(a.begin(), a.end());
        for (i = 0; i + 1 < n; i += 2) {
            if (a[i] > 0)
                break;
            if (a[i + 1] >= 0 && a[i] * -1 < a[i + 1])
                break;
            a[i] *= -1, a[i + 1] *= -1;
        }
        cout << accumulate(a.begin(), a.end(), 0ll) << '\n';
    }
    return (EXIT_SUCCESS);
}