/**
 * @file 1931e_aathdg.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Anna and the Valentine's Day
 * Gift(https://codeforces.com/problemset/problem/1931/E)
 * @version 0.1
 * @date 2024-10-07
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
    int t, n, m, dc, zc, ai, i;
    vector<int> zq;

    cin >> t;
    while (t--) {
        cin >> n >> m, dc = 0, zq.clear();
        for (i = 0; i < n; i++) {
            cin >> ai;
            zc = 0;
            while (!(ai % 10))
                zc++, ai /= 10;
            zc ? zq.push_back(zc) : void();
            while (ai)
                dc++, ai /= 10;
        }
        sort(zq.rbegin(), zq.rend());
        for (i = 0; i < zq.size() && dc < m + 1; i++)
            i % 2 ? dc += zq[i] : 0;
        cout << (dc >= m + 1 ? "Sasha\n" : "Anna\n");
    }
    return (EXIT_SUCCESS);
}