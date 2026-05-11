/*Có N hộ gia đình (1 ≤ N ≤ 1000). Mỗi hộ có số kWh tiêu thụ (số nguyên không âm).
Tính tiền điện cho từng hộ theo bậc thang cơ bản:
Bậc 1 (0-50 kWh): 1.678 đ/kWh.
Bậc 2 (51-100 kWh): 1.734 đ/kWh.
Bậc 3 (101-200 kWh): 2.014 đ/kWh.
Bậc 4 (201-300 kWh): 2.536 đ/kWh.
Bậc 5 (301-400 kWh): 2.834 đ/kWh.
Bậc 6 (401 kWh trở lên): 2.927 đ/kWh.

Sau đó áp dụng khuyến mãi:
Nếu tiền điện < 100,000 đồng: giảm 10% (làm tròn).
Ngược lại: không giảm.
In ra tổng tiền điện của tất cả hộ sau khuyến mãi (số nguyên).

Định dạng: Input:
Dòng đầu: số nguyên N. (Nếu số nguyên âm thì báo không hợp lệ!)
N dòng tiếp: mỗi dòng một số kWh của hộ.
Ví dụ: Input: 3 45 120 5
Output: 304509
Giải thích:
Hộ 1: 45 kWh → tiền = 75,510; khuyến mãi (vì < 100,000) → giảm 10% còn 67,959 (làm tròn).
Hộ 2: 120 kWh → tiền = 210,880; không giảm.
Hộ 3: 5 kWh → tiền = 8,390; khuyến mãi → giảm còn 7,551. Tổng: 67,959 + 210,880 + 7,551 = 286,390

Lưu ý: Output trong test cases dùng text không dấu.*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    const double gia_bac_1 = 1678;
    const double gia_bac_2 = 1734;
    const double gia_bac_3 = 2014;
    const double gia_bac_4 = 2536;
    const double gia_bac_5 = 2834;
    const double gia_bac_6 = 2927;

    int ho_gia_dinh;
    cin >> ho_gia_dinh;
    if (ho_gia_dinh < 0)
    {
        cout << "Khong hop le";
        return 1;
    }

    long long tong_tien_dien = 0;

    for (int i = 0; i < ho_gia_dinh; i++)
    {
        int kWh;
        double tien_dien = 0;

        cin >> kWh;

        if (kWh <= 50)
        {
            tien_dien = kWh * 1678;
        }
        else if (kWh <= 100)
        {
            tien_dien = 50 * 1678 + (kWh - 50) * 1734;
        }
        else if (kWh <= 200)
        {
            tien_dien = 50 * 1678 + 50 * 1734 + (kWh - 100) * 2014;
        }
        else if (kWh <= 300)
        {
            tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kWh - 200) * 2536;
        }
        else if (kWh <= 400)
        {
            tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kWh - 300) * 2834;
        }
        else
        {
            tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kWh - 400) * 2927;
        }

        if (tien_dien < 100000)
        {
            tien_dien = round(tien_dien * 0.9);
        }

        tong_tien_dien += (long long)tien_dien;
    }

    cout << tong_tien_dien << endl;

    return 0;
}