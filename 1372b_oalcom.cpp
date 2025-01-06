/**
 * @file 1372b_oalcom.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Omkar and Last Class of
 * Math(https://codeforces.com/problemset/problem/1372/B)
 * @version 0.1
 * @date 2025-01-06
 *
 * @copyright Copyright (c) 2025
 *
 */

#include <bits/stdc++.h>

#define ll long long

using namespace std;

vector<ll> get_primes(ll n) {
    vector<ll> primes;
    for (ll i = 2; i * i <= n; i++)
        if (n % i == 0) {
            primes.push_back(i);
            return primes;
        }
    if (n > 1)
        primes.push_back(n);
    return primes;
}

/**
 * @brief The main function
 *
 * @return int
 */
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t, n, i;

    cin >> t;
    while (t--) {
        cin >> n, i = 2;
        auto primes = get_primes(n);
        primes[0] == n
            ? cout << "1 " << n - 1 << "\n"
            : cout << n / primes[0] << " " << n - n / primes[0] << "\n";
    }
    return (EXIT_SUCCESS);
}