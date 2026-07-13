// The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n ≥ 2. 
// Given an integer N (0 ≤ N ≤ 20), print the first N terms of the Fibonacci sequence, separated by spaces. 
// If N = 0, print nothing (empty output).

// Input Format:
// A single integer N.

// Output Format:
// Print the first N Fibonacci numbers separated by spaces. No trailing space.

// Examples:
// Input: 5
// Output: 0 1 1 2 3

// Input: 1
// Output: 0

// Input: 0
// Output: (empty)

// Constraints: 0 ≤ N ≤ 20
// N is an integer.
// Note: Test outputs use plain ASCII without diacritics for technical reasons.
#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;

    long long a = 0, b = 1;

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            cout << " ";
        }
        cout << a;

        long long c = a + b;
        a = b;
        b = c;
    }
    cout << "\n";
    return 0;
}