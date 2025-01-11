/**
 * @file 1527b_pg.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Palindrome Game (easy
 * version)(https://codeforces.com/problemset/problem/1527/B)
 * @version 0.1
 * @date 2025-01-11
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
    ll t, n;
    string s;

    cin >> t;
    while (t--) {
        cin >> n >> s;
        cout << (n % 2 && count(s.begin(), s.end(), '0') != 1 && s[n / 2] == '0'
                     ? "ALICE"
                     : "BOB")
             << '\n';
    }
    return (EXIT_SUCCESS);
}