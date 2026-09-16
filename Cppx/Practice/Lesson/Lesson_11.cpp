#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using u128 = unsigned __int128;

// nhân modulo an toàn cho 64-bit
int64 mod_mul(int64 a, int64 b, int64 mod) {
    return (int64)((u128)a * b % mod);
}

// hàm luỹ thừa
int64 mod_pow(int64 base, int64 exp, int64 mod) {
    int64 res = 1 % mod;
    while (exp > 0) {
        if (exp & 1) res = mod_mul(res, base, mod);
        base = mod_mul(base, base, mod);
        exp >>= 1;
    }
    return res;
}

bool isPrime(int64 n) {
    if (n < 2) return false;
    static int64 smallPrimes[] = {2,3,5,7,11,13,17,19,23,29,31,37};
    for (int64 p : smallPrimes) {
        if (n == p) return true;
        if (n % p == 0) return false;
    }

    int64 d = n - 1;
    int s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }

    static int64 bases[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};

    for (int64 a : bases) {
        if (a % n == 0) continue;
        int64 x = mod_pow(a % n, d, n);
        if (x == 1 || x==n-1) continue;
        bool composite = true;
        for (int r = 1; r < s; ++r) {
            x = mod_mul(x, x, n);
            if (x == n-1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

int64 nearestPrime(int64 n) {
    if (n <= 2) {
        int64 x = 3;
        while (!isPrime(x)) ++x;
        return x;
    }
    for (int64 d = 1; ;++d) {
        int64 left = n - d;
        int64 right = n + d;
        if (isPrime(right)) return right;
        if (left >= 2 && isPrime(left)) return left;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        int64 N;
        cin >> N;
        if (isPrime(N)){
            cout << "YES " << nearestPrime(N) << "\n";
        } else {
            cout << "NO " << "\n";
        }
    }
    return 0;
}