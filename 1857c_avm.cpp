/**
 * @file 1857c_avm.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Assembly via
 * Minimums(https://codeforces.com/problemset/problem/1857/C)
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
    int t, n, i, temp, sa, ni;
    vector<int> a;
    map<int, int> bm;

    cin >> t;
    while (t--) {
        cin >> n, bm.clear();
        for (i = 0; i < (n * (n - 1)) / 2; i++) {
            cin >> temp;
            bm[temp]++;
        }
        a.resize(n), sa = n, i = 0;
        for (const auto bmi : bm) {
            a[i++] = bmi.first, sa--, ni = 1;
            while (sa * ni < bmi.second - (ni * (ni - 1)) / 2)
                a[i++] = bmi.first, sa--, ni++;
        }
        while (i < n)
            a[i++] = (*prev(bm.end())).first;
        for (const auto ai : a)
            cout << ai << ' ';
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}