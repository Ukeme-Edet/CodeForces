/**
 * @file 1673b_apbs.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem A Perfectly Balanced
 * String?(https://codeforces.com/problemset/problem/1673/B)
 * @version 0.1
 * @date 2025-01-21
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
    ll t, i, j, n;
    string s;

    cin >> t;
    while (t--) {
        cin >> s;
        n = s.size();
        set<char> st(s.begin(), s.end());

        for (i = 0; i <= n - st.size(); i++) {
            int fm[26]{0};
            for (j = i; j < i + st.size(); j++)
                fm[s[j] - 'a']++;
            for (j = 0; j < 26; j++)
                if (fm[j] > 1) {
                    cout << "NO\n";
                    break;
                }
            if (j < 26)
                break;
        }
        if (j == 26)
            cout << "YES\n";
    }
    return (EXIT_SUCCESS);
}