"""Cho một số nguyên dương n (2 ≤ n ≤ 10^6). 
Hãy phân tích n thành tích các thừa số nguyên tố và in ra kết quả theo định dạng: 
mỗi thừa số nguyên tố và số mũ tương ứng, phân tách bằng dấu cách, mỗi cặp trên một dòng. 
Nếu có nhiều thừa số, sắp xếp theo thứ tự tăng dần của thừa số nguyên tố.

Ví dụ:
Input: 12
Output:
2 2
3 1
Giải thích: 12 = 2^2 × 3^1

Input: 17
Output: 17 1
Giải thích: 17 là số nguyên tố nên chỉ có một thừa số

Ràng buộc: 2 ≤ n ≤ 10^6
Thời gian chạy: 1 giây
Bộ nhớ: 256 MB
Lưu ý về định dạng đầu ra: Các test case sử dụng văn bản không dấu (ASCII) để tránh lỗi kỹ thuật với JSON."""

n = int(input())

def la_so_nguyen_to(n):
    if n == 2:
        print("2 1")
        return 
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            print(f"{i} {count}")
        i += 1
    if n > 1:
        print(f"{n} 1")
    

la_so_nguyen_to(n)