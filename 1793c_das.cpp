/**
 * @file 1793c_das.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Dora and
 * Search(https://codeforces.com/problemset/problem/1793/C)
 * @version 0.1
 * @date 2024-10-20
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
    ll t, n, mav, miv, l, r;
    vector<ll> a;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        miv = 1, mav = n, l = 0, r = n - 1;
        while (l < r) {
            if (a[l] == miv || a[r] == miv) {
                a[l] == miv ? l++ : r--;
                miv++;
            } else if (a[l] == mav || a[r] == mav) {
                a[l] == mav ? l++ : r--;
                mav--;
            } else {
                cout << l + 1 << ' ' << r + 1 << '\n';
                break;
            }
        }
        if (l >= r)
            cout << "-1\n";
    }
    return (EXIT_SUCCESS);
}