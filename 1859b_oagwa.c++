/**
 * @file 1859b_oagwa.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Olya and Game with
 * Arrays(https://codeforces.com/problemset/problem/1859/B)
 * @version 0.1
 * @date 2024-10-09
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
    int t, n, m, i, temp, mi;
    vector<vector<int>> a;

    cin >> t;
    while (t--) {
        cin >> n, mi = INT_MAX;
        a.resize(n);
        for (i = 0; i < n; ++i) {
            cin >> m;
            a[i].resize(m);
            for (auto &ai : a[i]) {
                cin >> ai;
                mi = min(mi, ai);
            }
            sort(a[i].begin(), a[i].end());
        }
        sort(a.begin(), a.end(),
             [](const auto &a, const auto &b) { return a[1] < b[1]; });
        cout << accumulate(
                    a.begin(), a.end(), 0ll,
                    [](auto sum, const auto &vec) { return sum + vec[1]; }) -
                    a[0][1] + mi
             << '\n';
    }
    return (EXIT_SUCCESS);
}