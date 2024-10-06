/**
 * @file 1931d_dp.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Divisible
 * Pairs(https://codeforces.com/problemset/problem/1931/D)
 * @version 0.1
 * @date 2024-10-06
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
    long long n, x, y, ix, iy, yx, ans;
    vector<int> a;
    map<string, int> seen;

    cin >> t;
    while (t--) {
        cin >> n >> x >> y, ans = 0;
        a.resize(n), seen.clear();
        for (auto &ai : a)
            cin >> ai;
        for (auto ai : a) {
            ix = ai % x, iy = ai % y;
            ix == 0 ? yx = 0 : yx = x - ix;
            ans += seen[to_string(yx) + "," + to_string(iy)];
            seen[to_string(ix) + "," + to_string(iy)]++;
        }
        cout << ans << '\n';
    }
    return (EXIT_SUCCESS);
}