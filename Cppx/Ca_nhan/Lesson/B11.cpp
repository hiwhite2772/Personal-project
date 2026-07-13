// Viết chương trình nhập 10 số nguyên từ bàn phím và in ra mảng đó theo đúng thứ tự nhập. Mỗi số cách nhau một khoảng trắng.
// Đầu vào: 10 số nguyên, mỗi số trên một dòng.
// Đầu ra: In ra 10 số nguyên đã nhập, cách nhau bởi khoảng trắng.

// Ví dụ:
// Đầu vào:
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
// Đầu ra:
// 1 2 3 4 5 6 7 8 9 10

// Lưu ý:
// Đầu ra phải chính xác theo định dạng: các số cách nhau bởi khoảng trắng, không có khoảng trắng thừa ở đầu hoặc cuối.
// Test cases sử dụng văn bản không dấu để tránh lỗi kỹ thuật.

#include <iostream>
using namespace std;

int main()
{
    int arr[10];
    
    for (int i = 0; i < 10; i++)
    {
        cin >> arr[i];
    }
    for (int i = 0; i < 10; i++)
    {
        cout << arr[i] << ' ';
    }
    return 0;
}