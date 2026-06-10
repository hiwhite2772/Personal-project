/* Viết chương trình nhận vào số nguyên n (1 ≤ n ≤ 1000) là số học sinh, sau đó nhận n dòng,
mỗi dòng chứa một số thực là điểm số của học sinh (từ 0 đến 10).
In ra số lượng học sinh đạt từng loại A, B, C, D, E, F theo quy tắc tương tự bài dễ.
Nếu có điểm không hợp lệ (ngoài 0-10), bỏ qua học sinh đó và không đếm vào bất kỳ loại nào.
Đầu ra gồm 6 số nguyên cách nhau bởi dấu cách: số lượng A, B, C, D, E, F.

Ví dụ:
Input:
3
8.5
4.0
9.0
Output:
2 0 0 1 0 0
Giải thích: Có 1 điểm A (9.0), 1 điểm A (8.5), 1 điểm F (4.0).

Lưu ý: Đầu ra chỉ chứa số, không có chữ cái. */

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count[6] = {0};  // Tạo danh sách ban đầu
    for (int i = 0; i < n; i++)
    {
        float diem;
        char ketqua;
        cin >> diem;

        if (diem < 0 || diem > 10)
        {
            continue;
        }

        if (diem >= 8.5)
        {
            count[0]++; // Điểm chữ A
        }
        else if (diem >= 7)
        {
            count[1]++; // Điểm chữ B
        }
        else if (diem >= 5.5)
        {
            count[2]++; // Điểm chữ C
        }
        else if (diem >= 4)
        {
            count[3]++; // Điểm chữ D
        }
        else if (diem >= 2.5)
        {
            count[4]++;
        }
        else
        {
            count[5]++; // Điểm chữ F
        }
    }
    for (int i = 0; i < 6; i++)
    {
        cout << count[i];
        if (i < 5)
        {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}