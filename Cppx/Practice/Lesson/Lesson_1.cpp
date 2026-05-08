/*Bạn được cho một giá trị nhiệt độ theo độ Celsius (độ C).
Hãy chuyển đổi nó sang độ Fahrenheit (độ F) theo công thức: F = C × 9/5 + 32.
Đầu vào: Một số thực duy nhất biểu thị nhiệt độ theo độ C.
Đầu ra: Một số thực (có thể là số nguyên nếu kết quả là số nguyên) biểu thị nhiệt độ theo độ F, làm tròn đến 2 chữ số thập phân.

Ví dụ:
Đầu vào: 0  Đầu ra: 32.00  Giải thích: 0 × 9/5 + 32 = 32
Đầu vào: 100  Đầu ra: 212.00  Giải thích: 100 × 9/5 + 32 = 212
Đầu vào: -40  Đầu ra: -40.00  Giải thích: -40 × 9/5 + 32 = -40
Ràng buộc: Giá trị đầu vào nằm trong khoảng [-273.15, 1000].

Lưu ý: Đầu ra phải được định dạng chính xác với 2 chữ số thập phân (ví dụ: sử dụng printf với %.2f trong C/C++).
Trong các test case, đầu ra sử dụng văn bản không dấu để tránh lỗi kỹ thuật.*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float celsius;
    float fahrenheit;
    
    cin >> celsius;

    fahrenheit = (celsius * 9.0/5.0) + 32.0;

    printf("%.2f", fahrenheit);
    return 0;
}