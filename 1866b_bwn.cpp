#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
const int MOD = 998244353;
 
int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
 
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for (int& p : a) cin >> p;
    for (int& p : b) cin >> p;
 
    map<int, int> mp1;  
    for (int i = 0; i < n; i++) 
        mp1[a[i]] = b[i];
 
    int m;
    cin >> m;
    vector<int> c(m), d(m);
    for (int& p : c) cin >> p;
    for (int& p : d) cin >> p;
 
    map<int, int> mp2;
    for (int i = 0; i < m; i++) { 
        if (!mp1.count(c[i])) {
            cout << "0\n";
            return 0;
        }
        if (d[i] > mp1[c[i]]) {
            cout << "0\n";
            return 0;
        }
        mp2[c[i]] = d[i];
    }
 
    int res = 1;
    for (int i = 0; i < n; i++) {
        if (!mp2.count(a[i])) {
            res = (1ll * res * 2) % MOD; 
        } else {
            int d = b[i] - mp2[a[i]];
            if (d > 0)
                res = (1ll * res * 2) % MOD;
        }
    }
 
    cout << res << '\n';
    return 0;
}