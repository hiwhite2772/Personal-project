// Bạn được cho một số nguyên dương n. Hãy kiểm tra xem n có phải là số nguyên tố hay không.
// Nếu n là số nguyên tố, in ra “YES”, ngược lại in ra “NO”.
// Input: Một dòng duy nhất chứa số nguyên n (1 ≤ n ≤ 10^6).
// Output: In ra “YES” hoặc “NO”.

// Ví dụ:
// Input: 7
// Output: YES

// Input: 10
// Output: NO

// Giới hạn: 1 ≤ n ≤ 10^6
// Số nguyên tố là số tự nhiên lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
// Lưu ý: Các test case sử dụng văn bản không dấu (ví dụ: “YES”, “NO”) để tránh lỗi kỹ thuật.

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    bool isprime = true;
    if (n < 2) {
        isprime = false;
    }
    
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            isprime = false;
        }
    }

    if (isprime) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}
