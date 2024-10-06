/**
 * @file 1914d_ta.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Three
 * Activities(https://codeforces.com/problemset/problem/1914/D)
 * @version 0.1
 * @date 2024-10-06
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
    int t, n, i, j, k, ans, tans;
    set<int> days;
    vector<pair<int, int>> a, b, c;

    cin >> t;
    while (t--) {
        cin >> n, ans = i = j = k = 0;
        a.resize(n), b.resize(n), c.resize(n);
        for (auto &ai : a) {
            cin >> ai.first;
            ai.second = i++;
        }
        for (auto &bi : b) {
            cin >> bi.first;
            bi.second = j++;
        }
        for (auto &ci : c) {
            cin >> ci.first;
            ci.second = k++;
        }
        sort(a.rbegin(), a.rend()), sort(b.rbegin(), b.rend()),
            sort(c.rbegin(), c.rend());
        for (i = 0; i < 3; i++)
            for (j = 0; j < 3; j++)
                for (k = 0; k < 3; k++) {
                    days = set<int>({a[i].second, b[j].second, c[k].second});
                    tans = a[i].first + b[j].first + c[k].first;
                    days.size() == 3 ? ans = max(ans, tans) : 0;
                }
        cout << ans << '\n';
    }
    return (EXIT_SUCCESS);
}