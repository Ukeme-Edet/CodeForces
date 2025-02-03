/**
 * @file 1614b_daanp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Divan and a New
 * Project(https://codeforces.com/problemset/problem/1614/B)
 * @version 0.1
 * @date 2024-09-01
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long t, n, i, s, res;
    vector<int> b;
    vector<pair<int, int>> a;

    cin >> t;
    while (t--) {
        cin >> n, i = 0;
        a.resize(n), b.resize(n);
        for (auto &ai : a) {
            cin >> ai.first;
            ai.second = i++;
        }
        sort(a.begin(), a.end(),
             [](auto a, auto b) { return a.first > b.first; });
        s = 1, i = 0, res = 0;
        for (auto &ai : a) {
            b[ai.second] = s, i++, res += ai.first * abs(s);
            i % 2 ? s *= -1 : s < 0 ? s = s * -1 + 1 : s + 1;
        }
        cout << res * 2 << '\n';
        cout << 0 << ' ';
        for (auto bi : b)
            cout << bi << ' ';
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}