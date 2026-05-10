/*
Mở rộng từ bài toán cơ bản: sau khi tính BMI, phân loại theo tiêu chuẩn WHO:
BMI < 18.5: "Thieu can"
18.5 ≤ BMI < 25: "Binh thuong"
25 ≤ BMI < 30: "Thua can"
BMI ≥ 30: "Beo phi"
Yêu cầu: Đọc hai số thực cân nặng (kg) và chiều cao (m).
Tính BMI làm tròn 1 chữ số thập phân, sau đó in ra BMI và phân loại cách nhau bởi dấu cách.

Ví dụ:
Input: 70 1.75
Output: 22.9 Binh thuong
Giải thích: BMI = 22.9 thuộc khoảng [18.5, 25) → "Binh thuong"

Lưu ý: Đầu vào luôn hợp lệ (số dương). Phân loại in ra không dấu (theo quy ước kỹ thuật).
Lưu ý kỹ thuật: Đầu ra test sử dụng văn bản không dấu để tránh lỗi mã hóa.
*/

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    float weight, height;
    cin >> weight >> height;

    if (height == 0) {
        cout << "Khong the chia so 0\n";
        return 1;
    }

    cout << fixed << setprecision(1);
    float bmi = weight / pow(height, 2);
    cout << bmi << " ";

    if (bmi < 18.5) {
        cout << "Thieu can" <<"\n";
    } else if (18.5 <= bmi && bmi < 25) {
        cout << "Binh thuong" << "\n";
    } else if (25 <= bmi && bmi < 30) {
        cout << "Thua can" << "\n";
    } else {
        cout << "Beo phi" << "\n";
    }
    return 0;
}