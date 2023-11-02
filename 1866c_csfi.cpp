#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
const int MOD = 998244353;
 
int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
 
    int n;
    cin >> n;
 
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        for (int j = 0; j < x; j++) {
            int to;
            cin >> to;
            --to;
            int w;
            cin >> w;
            adj[i].emplace_back(to, w);
        }
    }
 
    vector<vector<int>> dp(n, vector<int>(2));
    vector<int> sub_invs(n);
    vector<bool> vis(n);
 
    int res = 0;
 
    vector<int> child;
    const auto dfs = [&](auto&& self, int source) -> void {
        vis[source] = true;
        for (const auto& [to, w] : adj[source]) {
            if (!vis[to])
                self(self, to);
            res += sub_invs[to];
            res %= MOD;
            res += (1ll * dp[source][1] * dp[to][0]) % MOD;
            res %= MOD;
            if (w == 0) {
                res += dp[source][1];
                res %= MOD;
            } else {
                sub_invs[source] += dp[to][0];
                sub_invs[source] %= MOD;
            }
            dp[source][w]++;
            dp[source][w] %= MOD;
            dp[source][0] += dp[to][0];
            dp[source][0] %= MOD;
            dp[source][1] += dp[to][1];
            dp[source][1] %= MOD;
        }   
    };
    dfs(dfs, 0);
 
    res += sub_invs[0];
    res %= MOD;
 
    cout << res << '\n';
 
    return 0;
}