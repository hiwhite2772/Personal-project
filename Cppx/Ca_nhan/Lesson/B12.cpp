#include <bits/stdc++.h>
using namespace std;

string thapPhanSangNhiPhan(int n) {
    if (n == 0) return "0";

    string kq = "";
    while (n > 0) {
        int du = n % 2;
        kq = char('0' + du) + kq;
        n /= 2;
    }
    return kq;
}

void solve() {
    int n;
    cin >> n;
    cout << thapPhanSangNhiPhan(n);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}