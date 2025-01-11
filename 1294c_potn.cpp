/**
 * @file 1294c_potn.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Product of Three
 * Numbers(https://codeforces.com/problemset/problem/1294/C)
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
    ll t, n, i, j, p, nc;
    vector<ll> ps, tres, res(2);
    map<ll, bool> ip;

    for (i = 2; i < 100000; i++) {
        if (ip[i])
            continue;
        ps.push_back(i);
        for (j = i * i; j < 100000; j += i)
            ip[j] = 1;
    }
    cin >> t;
    while (t--) {
        cin >> n, tres.clear();
        nc = n;
        for (i = 0; i < ps.size(); i++) {
            while (n % ps[i] == 0) {
                n /= ps[i];
                tres.push_back(ps[i]);
            }
        }
        if (n > 1)
            tres.push_back(n);
        p = tres[0];
        res[0] = res[1] = 0;
        for (i = 1, j = 0; i < tres.size() && j < 2; i++) {
            if (p != res[0] && p != res[1]) {
                res[j++] = p;
                p = tres[i];
            } else
                p *= tres[i];
        }
        if (j < 2 ||
            find(res.begin(), res.end(), nc / (res[0] * res[1])) != res.end())
            cout << "NO\n";
        else
            cout << "YES\n"
                 << res[0] << ' ' << res[1] << ' ' << nc / (res[0] * res[1])
                 << '\n';
    }
    return (EXIT_SUCCESS);
}