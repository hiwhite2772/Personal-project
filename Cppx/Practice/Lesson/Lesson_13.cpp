#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    int guess;
    while (cin >> guess) {
        if (guess == 0) break;
        if (guess > n) {
            cout << "CAO" << "\n";
        } else if (guess < n) {
            cout << "THAP" << "\n";
        } else {
            cout << "TRUNG" << "\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}