#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(string s) {
    int i = 0;
    int j = s.length() - 1;
    while (i < j) {
        if (s[i] != s[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

void solve() {
    string s, t;

    getline(cin, s);
    for (char c : s) {
        if (isalnum((unsigned char) c)) {
            t += tolower((unsigned char) c);
        }
    }

    if (isPalindrome(t) == true) {
        cout << "YES" << "\n";
    } else {
        cout << "NO" << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}