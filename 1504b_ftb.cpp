/**
 * @file 1504b_ftb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Flip the
 * Bits(https://codeforces.com/problemset/problem/1504/B)
 * @version 0.1
 * @date 2025-01-16
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
    ll t, n, oc, zc, i, ocm, zcm, f;
    string a, b;

    cin >> t;
nxt:
    while (t--) {
        cin >> n >> a >> b;
        i = n - 1, f = 0;
        oc = zc = 0;
        while (i >= 0) {
            while (i >= 0 && a[i] == b[i])
                i--;
            while (i >= 0 && a[i] != b[i]) {
                zc += a[i] == '0', oc += a[i] == '1';
                i--;
            }
            if (zc != oc) {
                cout << "NO\n";
                goto nxt;
            }
            zc = oc = 0;
            while (i >= 0 && a[i] == b[i]) {
                zc += a[i] == '0', oc += a[i] == '1';
                i--;
            }
            if (zc != oc) {
                cout << "NO\n";
                goto nxt;
            }
            zc = oc = 0;
        }
        cout << (oc || zc ? "NO\n" : "YES\n");
        cout.flush();
    }
    return (EXIT_SUCCESS);
}