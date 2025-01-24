/**
 * @file 1618c_pta.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Paint the
 * Array(https://codeforces.com/problemset/problem/1618/C)
 * @version 0.1
 * @date 2025-01-24
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
    ll t, n, a[100], i, g1, g2;
    bool e, o;

    cin >> t;
    while (t--) {
        cin >> n;
        for (i = 0; i < n; i++)
            cin >> a[i];
        g1 = a[0], g2 = a[1];
        for (i = 0; i < n; i++)
            if (i % 2)
                g2 = gcd(g2, a[i]);
            else
                g1 = gcd(g1, a[i]);
        e = o = 1;
        for (i = 0; i < n; i++)
            e &= (!(i % 2) || a[i] % g1), o &= (i % 2 || a[i] % g2);
        if (e)
            cout << g1;
        else if (o)
            cout << g2;
        else
            cout << 0;
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}