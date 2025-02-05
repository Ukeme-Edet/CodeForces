/**
 * @file 1155a_ras.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Reverse a
 * Substring(https://codeforces.com/problemset/problem/1155/A)
 * @version 0.1
 * @date 2024-09-02
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
    int n, cm[26], i, j;
    string s;

    cin >> n >> s;
    memset(cm, 0, sizeof(int) * 26);
    for (j = n - 1; j >= 0; j--) {
        for (i = s[j] - 1; i >= 'a'; i--)
            if (cm[i - 'a']) {
                cout << "YES\n" << j + 1 << ' ' << cm[i - 'a'] + 1 << '\n';
                return (EXIT_SUCCESS);
            }
        cm[s[j] - 'a'] = j;
    }
    cout << "NO\n";
    return (EXIT_SUCCESS);
}