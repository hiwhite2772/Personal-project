#include <bits/stdc++.h>
using namespace std;

string solve() {
    string S;
    getline(cin, S);

    stringstream ss(S);
    string word;
    string result = "";
    while (ss >> word) {
        result += toupper(word[0]);
    }
    return result + "\n";
}

int main() {
    int T;
    if (!(cin>>T)) return 0;
    cin.ignore();
    while (T--){
        cout << solve();
    }
    return 0;
}