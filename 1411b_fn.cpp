/**
 * @file 1411b_fn.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Fair
 * Numbers(https://codeforces.com/problemset/problem/1411/B)
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
    long long t, n, nc;

    cin >> t;
    while (t--) {
        cin >> n;
        while (true) {
            nc = n;
            while (nc) {
                if ((nc % 10) && n % (nc % 10))
                    break;
                nc /= 10;
            }
            if (!nc) {
                cout << n << '\n';
                break;
            }
            n++;
        }
    }
    return (EXIT_SUCCESS);
}