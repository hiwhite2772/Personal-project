#include <bits/stdc++.h>
using namespace std;

long long tinh_tong_uoc(long long n) {
    if (n == 1) {
        return 1;
    }
    long long tong_thanh_phan, luy_thua;
    long long tong_uoc = 1;
    long long temp = n;
    if (temp % 2 == 0) {
        tong_thanh_phan = 1;
        luy_thua = 1;
        while (temp % 2 == 0) {
            luy_thua *= 2;
            tong_thanh_phan += luy_thua;
            temp /= 2;
        }
        tong_uoc *= tong_thanh_phan;
    }
    long long p = 3;
    while (p*p <= temp) {
        if (temp % p == 0) {
            tong_thanh_phan = 1;
            luy_thua = 1;
            while (temp % p == 0) {
                luy_thua *= p;
                tong_thanh_phan += luy_thua;
                temp /= p;
            }
            tong_uoc *= tong_thanh_phan;
        }
        p +=2;
    }
    if (temp > 1) {
        tong_uoc *= (1 + temp);
    }
    return tong_uoc;
}

int main(){
    int T;
    if(!(cin>>T)) return 0;
    while (T--)
    {
        long long N;
        cin >> N;
        cout << tinh_tong_uoc(N) << '\n';
    }
    return 0;
}
