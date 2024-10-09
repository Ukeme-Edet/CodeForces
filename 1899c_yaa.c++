/**
 * @file 1899c_yaa.c++
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Yarik and
 * Array(https://codeforces.com/problemset/problem/1899/C)
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
    int t, n, i, res, cs;
    vector<int> a;

    cin >> t;
    while (t--) {
        cin >> n;
        a.resize(n);
        for (auto &ai : a)
            cin >> ai;
        res = cs = a[0];
        for (i = 1; i < n; i++) {
            if ((abs(a[i]) % 2 == abs(a[i - 1]) % 2) || cs < 0)
                cs = 0;
            cs += a[i];
            res = max(cs, res);
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}