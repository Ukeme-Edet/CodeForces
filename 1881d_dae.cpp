/**
 * @file 1881d_dae.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Divide and
 * Equalize(https://codeforces.com/problemset/problem/1881/D)
 * @version 0.1
 * @date 2024-10-09
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief Generates a list of prime numbers up to a given limit.
 *
 * This function uses the Sieve of Eratosthenes algorithm to find all prime
 * numbers up to a specified number `n`. It initializes a boolean vector to mark
 * non-prime numbers and iterates through the vector to mark multiples of each
 * prime number.
 *
 * @param n The upper limit (inclusive) up to which prime numbers are to be
 * found.
 * @return A vector containing all prime numbers up to `n`.
 */
vector<long long> get_primes(long long n) {
    long long i, j;
    vector<bool> pb(n + 1, 1);
    vector<long long> primes;

    for (i = 2; i <= n; i++)
        if (pb[i])
            for (j = i * i; j <= n; j += i)
                pb[j] = 0;
    for (i = 2; i <= n; i++)
        pb[i] ? primes.push_back(i) : void();
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
    long long t, n, i, j, temp, p, f;
    map<long long, long long> pfm;
    const vector<long long> primes = get_primes(10000);

    cin >> t;
    while (t--) {
        cin >> n, pfm.clear(), p = 1;
        for (i = 0; i < n; i++) {
            cin >> temp;
            j = 0;
            while (temp > 1 && pow(primes[j], 2) <= temp) {
                f = primes[j];
                while (!(temp % f))
                    pfm[f]++, temp /= f;
                j++;
            }
            if (temp > 1)
                pfm[temp]++;
        }
        for (const auto mfmi : pfm)
            if (mfmi.second % n) {
                cout << "NO", p = 0;
                break;
            }
        cout << (p ? "YES\n" : "\n");
    }
    return (EXIT_SUCCESS);
}