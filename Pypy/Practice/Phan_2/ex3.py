"""Viết chương trình nhận ba số nguyên dương a, b, và c (1 ≤ a ≤ b ≤ 20, 1 ≤ c ≤ 10).
In bảng cửu chương từ a đến b, mỗi bảng in từ 1 đến c.
Đầu ra phải theo định dạng: mỗi dòng chứa nhiều phép nhân, cách nhau bởi dấu tab (\t).
Cụ thể, in theo từng hàng của i từ 1 đến c: trên mỗi hàng, in tất cả phép nhân n x i với n từ a đến b, mỗi phép nhân cách nhau bởi tab.

Ví dụ:
Đầu vào: 2 4 3
Đầu ra:
2 x 1 = 2 3 x 1 = 3 4 x 1 = 4
2 x 2 = 4 3 x 2 = 6 4 x 2 = 8
2 x 3 = 6 3 x 3 = 9 4 x 3 = 12

Nếu đầu vào không hợp lệ, in ‘Dau vao khong hop le’.
Lưu ý: Đầu ra test sử dụng văn bản không dấu để tránh lỗi kỹ thuật."""

input_str = input().strip()

try:
    parts = input_str.split()
    if len(parts) != 3:
        print("Dau vao khong hop le")
        exit()
    else:
        a, b, c = map(int, parts)
        if not (1 <= a <= b <= 20 and 1 <= c <= 10):
            print("Dau vao khong hop le")
        else:
            for i in range(1, c+1):
                row_output = []
                for n in range(a, b+1):
                    row_output.append(f"{n} x {i} = {i*n}")
                print("\t".join(row_output))
except ValueError:
    print("Dau vao khong hop le")