/**
 * @file 1567b_mm.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem MEXor
 * Mixup(https://codeforces.com/problemset/problem/1567/B)
 * @version 0.1
 * @date 2024-08-31
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
    int t, a, b, res, i;
    map<int, int> pcxor;

    for (i = 1, res = 0; i <= 300000; i++) {
        pcxor[i] = res;
        res ^= i;
    }

    cin >> t;
    while (t--) {
        cin >> a >> b;
        if (pcxor[a] == b)
            cout << a;
        else
            (pcxor[a] ^ b) != a ? cout << a + 1 : cout << a + 2;
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}
