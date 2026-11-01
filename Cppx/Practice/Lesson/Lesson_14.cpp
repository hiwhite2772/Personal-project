#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int count_odd = 0, count_even = 0;
    long long total_odd = 0, total_even = 0;

    for (int i = 0; i < n; i++){
        if (a[i] % 2 == 0) {
            total_even += a[i];
            count_even++;
        }

        if (a[i] % 2 != 0) {
            total_odd += a[i];
            count_odd++;
        }
    }
    double average_odd, average_even;
    
    if (count_even == 0 ) {
        average_even = 0;
    } else {
        average_even = (double)total_even / count_even;
    }
    
    if (count_odd == 0) {
        average_odd = 0;
    } else {
        average_odd = (double)total_odd / count_odd;
    }
    
    cout << fixed << setprecision(2);
    cout << total_even << " " << average_even << " " << total_odd << " " << average_odd;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}