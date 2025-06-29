/**
 * @file 1543a_eb.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Exciting
 * Bets(https://codeforces.com/problemset/problem/1543/A)
 * @version 0.1
 * @date 2024-08-30
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
    short t;
    long long a, b, res;

    cin >> t;
    while (t--) {
        cin >> a >> b;
        if (a == b)
            cout << "0 0\n";
        else {
            res = abs(a - b);
            cout << res << ' ' << min(a % res, res - a % res) << '\n';
        }
    }
    return (EXIT_SUCCESS);
}