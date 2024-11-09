/**
 * @file 1742e_scuza.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem
 * Scuza(https://codeforces.com/problemset/problem/1742/E)
 * @version 0.1
 * @date 2024-11-09
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
    ll t, n, q, ki, i;
    vector<ll> a, ms, ps;

    cin >> t;
    while (t--) {
        cin >> n >> q;
        a.resize(n), ms.resize(n + 1), ps.resize(n + 1);
        ms[0] = 0, ps[0] = 0, i = 0;
        for (auto &ai : a) {
            cin >> ai;
            ms[i + 1] = max(ms[i], ai);
            ps[i + 1] = ps[i] + ai;
            i++;
        }
        while (q--) {
            cin >> ki;
            i = upper_bound(ms.begin(), ms.end(), ki) - ms.begin();
            cout << ps[i - 1] << ' ';
        }
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}