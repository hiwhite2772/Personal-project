/*Viết chương trình nhập số nguyên n (1 ≤ n ≤ 100) là số lượng hình tròn. Sau đó nhập n số thực rᵢ là bán kính của từng hình tròn.
Tính diện tích Sᵢ và chu vi Cᵢ cho mỗi hình tròn theo công thức:
Sᵢ = π * rᵢ²
Cᵢ = 2 * π * rᵢ
Với π = 3.14159.

Yêu cầu đầu vào/ra:
Đầu vào: Dòng đầu tiên chứa số nguyên n. n dòng tiếp theo, mỗi dòng chứa một số thực rᵢ (0 ≤ rᵢ ≤ 1000).
Đầu ra: Với mỗi hình tròn, in ra hai số thực Sᵢ và Cᵢ trên một dòng, cách nhau bởi dấu cách, làm tròn đến 2 chữ số thập phân.
Ví dụ:

Đầu vào:
3
5
0
10.5

Đầu ra:
78.54 31.42
0.00 0.00
346.36 65.97

Giải thích:
Hình 1: r = 5 → S ≈ 78.54, C ≈ 31.42
Hình 2: r = 0 → S = 0.00, C = 0.00
Hình 3: r = 10.5 → S ≈ 346.36, C ≈ 65.97

Lưu ý:
Sử dụng π = 3.14159.
Đảm bảo làm tròn đến 2 chữ số thập phân.
Test outputs sử dụng văn bản không dấu để tránh lỗi kỹ thuật.*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    const double PI = 3.14159;
    int n;
    cin >> n;
    cout << fixed << setprecision(2);

    for (int i = 0; i < n; i++)
    {
        double r, area, cir;
        cin >> r;
        area = PI * r * r;
        cir = 2 * PI * r;
        cout << area << " " << cir << "\n";
        return 0;
    }
}