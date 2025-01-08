/**
 * @file 1539c_sg.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Stable
 * Groups(https://codeforces.com/problemset/problem/1539/C)
 * @version 0.1
 * @date 2025-01-08
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
    ll n, k, x, i, res;
    vector<ll> a, br;

    cin >> n >> k >> x, res = 0;
    a.resize(n);
    for (auto &ai : a)
        cin >> ai;
    sort(a.begin(), a.end());
    for (i = 0; i < n - 1; i++)
        if (a[i + 1] - a[i] > x)
            br.push_back(a[i + 1] - a[i]), res++;
    sort(br.begin(), br.end());
    for (const auto &bri : br) {
        k -= (bri - 1) / x;
        if (k < 0)
            break;
        res--;
    }
    cout << res + 1 << '\n';
    return (EXIT_SUCCESS);
}