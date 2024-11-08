/**
 * @file 1775b_gata.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Gardener and the
 * Array(https://codeforces.com/problemset/problem/1775/B)
 * @version 0.1
 * @date 2024-11-08
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
    ll t, n, nb;
    vector<vector<ll>> c;
    map<ll, ll> bc;

    cin >> t;
next:
    while (t--) {
        cin >> n;
        c.resize(n), bc.clear();
        for (auto &ci : c) {
            cin >> nb;
            ci.resize(nb);
            for (auto &cii : ci) {
                cin >> cii;
                bc[cii]++;
            }
        }
        for (const auto &ci : c)
            if (all_of(ci.begin(), ci.end(),
                       [&bc](auto a) { return bc[a] > 1; })) {
                cout << "Yes\n";
                goto next;
            }
        cout << "No\n";
    }
    return (EXIT_SUCCESS);
}