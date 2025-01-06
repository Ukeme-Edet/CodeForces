/**
 * @file 1820b_jia.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem JoJo's Incredible
 * Adventures(https://codeforces.com/problemset/problem/1820/B)
 * @version 0.1
 * @date 2025-01-03
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
    ll t, res, l, r, i;
    string s;

    cin >> t;
    while (t--) {
        cin >> s;
        if (all_of(s.begin(), s.end(), [](char c) { return c == '0'; })) {
            cout << "0\n";
            continue;
        }
        if (all_of(s.begin(), s.end(), [](char c) { return c == '1'; })) {
            cout << s.size() * s.size() << '\n';
            continue;
        }
        if (s.find('0') != string::npos && s[0] == '1' &&
            s[s.size() - 1] == '1')
            s = s.substr(s.find('0')) + s.substr(0, s.find('0'));
        l = r = res = 0;
        while (r < s.size()) {
            while (l < s.size() && s[l] == '0')
                l++;
            r = l;
            while (r < s.size() && s[r] == '1')
                r++;
            for (i = r - l; i > 0; i--)
                res = max(res, i * (r - l - i + 1));
            l = r;
        }
        cout << res << '\n';
    }
    return (EXIT_SUCCESS);
}