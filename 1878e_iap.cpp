/**
 * @file 1878e_iap.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Iva &
 * Pav(https://codeforces.com/problemset/problem/1878/E)
 * @version 0.1
 * @date 2024-11-17
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

#define ll long long

using namespace std;

pair<ll, ll> find_pair(const vector<pair<ll, ll>> &inter, ll l) {
    ll low = 0, high = inter.size() - 1, mid;

    while (low <= high) {
        mid = low + (high - low) / 2;
        if (inter[mid].first <= l && inter[mid].second >= l)
            return inter[mid];
        else if (inter[mid].first > l)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return {-1, -1};
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t, n, q, l, k, i, j, s, res;
    pair<ll, ll> xx;
    vector<ll> a;
    vector<vector<pair<ll, ll>>> bm;

    cin >> t;
    while (t--) {
        cin >> n, bm.clear();
        a.resize(n), bm.resize(32);
        for (auto &ai : a)
            cin >> ai;
        for (i = 0; i < 32; i++) {
            for (j = 0; j < n; j++) {
                if (a[j] & (1 << i)) {
                    s = j;
                    while (j < n && (a[j] & (1 << i)))
                        j++;
                    bm[i].push_back({s, j - 1});
                }
            }
        }
        cin >> q;
        while (q--) {
            cin >> l >> k;
            res = -1, s = 0, i = 31;
            while (!(k & (1 << i)) && i >= 0)
                res = max(res, find_pair(bm[i--], l - 1).second);
            j = LLONG_MAX;
            while (i >= 0) {
                xx = find_pair(bm[i], l - 1);
                if (k & (1 << i))
                    j = min(j, xx.second);
                else
                    res = max(res, min(xx.second, j));
                i--;
            }
            if (i == -1)
                res = max(res, j);
            cout << (res >= l - 1 ? res + 1 : -1) << ' ';
        }
        cout << '\n';
    }
    return (EXIT_SUCCESS);
}