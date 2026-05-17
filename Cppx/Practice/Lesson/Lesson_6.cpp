/* Viết chương trình đọc số nguyên n (1 ≤ n ≤ 100) là số lượng phương trình cần giải, sau đó đọc n dòng,
mỗi dòng chứa hai số nguyên a và b. Với mỗi phương trình ax + b = 0, in ra nghiệm:
Nếu a ≠ 0: in nghiệm x dưới dạng phân số tối giản p/q (với q > 0). Nếu x là số nguyên, in dưới dạng p/1.
Nếu a = 0 và b ≠ 0: in "VO NGHIEM".
Nếu a = 0 và b = 0: in "VO SO NGHIEM".

Ví dụ: Input: 3 2 -4 0 5 0 0 Output: 2/1 VO NGHIEM VO SO NGHIEM
Giải thích:
Phương trình 2x - 4 = 0 có nghiệm x = 2 → in "2/1".
Phương trình 0x + 5 = 0 vô nghiệm → in "VO NGHIEM".
Phương trình 0x + 0 = 0 vô số nghiệm → in "VO SO NGHIEM".

Ràng buộc:
1 ≤ n ≤ 100
-1000 ≤ a, b ≤ 1000
a và b là số nguyên.
Lưu ý: Đầu ra trong test cases sử dụng văn bản không dấu. */

#include <iostream>
#include <cmath>
using namespace std;

int gcd(int a, int b)
{
    a = abs(a);
    b = abs(b);
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int a, b, x;
        cin >> a >> b;
        if (a == 0)
        {
            if (b == 0)
            {
                cout << "VO SO NGHIEM" << "\n";
            }
            else
            {
                cout << "VO NGHIEM" << "\n";
            }
        }
        else
        {
            int p = -b;
            int q = a;
            int g = gcd(p, q);
            p /= g;
            q /= g;
            if (q < 0)
            {
                p = -p;
                q = -q;
            }
            cout << p << "/" << q << "\n";
        }
    }

    return 0;
}