/*
Bạn được cho một thời gian dưới dạng ba số nguyên: giờ, phút, giây, nhưng giờ có thể lớn hơn 23 (ví dụ: đại diện cho thời gian tích lũy). Hãy tính tổng số giây tương ứng.

Đầu vào:
Một dòng chứa ba số nguyên h, m, s cách nhau bởi dấu cách, lần lượt là giờ, phút, giây (0 ≤ h ≤ 10^6, 0 ≤ m ≤ 59, 0 ≤ s ≤ 59).

Đầu ra:
Một số nguyên duy nhất là tổng số giây. Lưu ý: kết quả có thể rất lớn, đảm bảo sử dụng kiểu dữ liệu phù hợp.

Ví dụ: 
Đầu vào: 25 30 45
Đầu ra: 91845
Giải thích: 25 giờ = 90000 giây, 30 phút = 1800 giây, 45 giây = 45 giây --> Tổng: 90000 + 1800 + 45 = 91845 giây.

Lưu ý: Trong các test case, đầu ra sử dụng văn bản không dấu để tránh lỗi kỹ thuật.
*/

#include <iostream>
using namespace std;

int main(){
    
    long long h, m, s;
    cin >> h >> m >> s;
    long long total = h * 3600 + m * 60 + s;
    cout<< total << "\n";

    return 0;
}