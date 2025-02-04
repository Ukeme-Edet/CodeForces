/**
 * @file 1485a_aad.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Add and
 * Divide(https://codeforces.com/problemset/problem/1485/A)
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
    int t, a, b, res, i, q, ac;

    cin >> t;
    while (t--) {
        cin >> a >> b, res = INT_MAX, i = 0;

        b == 1 ? b++, i++ : 0;
        do {
            ac = a, q = 0;
            while (ac)
                ac /= b, q++;
            res = min(res, i + q);
            b++, i++;
        } while (i < res);
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}