"""Cho hai dictionary A và B, mỗi dictionary chứa các cặp khóa-giá trị với khóa là chuỗi và giá trị là số nguyên. Hãy kết hợp chúng thành một dictionary mới theo quy tắc:
Nếu một khóa chỉ xuất hiện trong A hoặc B, giữ nguyên cặp khóa-giá trị đó.
Nếu một khóa xuất hiện trong cả A và B, giá trị mới là tổng của hai giá trị.

Đầu vào:
Dòng đầu tiên: Số nguyên n (1 ≤ n ≤ 100) - số cặp trong dictionary A. n dòng tiếp theo: Mỗi dòng chứa một chuỗi khóa và một số nguyên giá trị, cách nhau bởi dấu cách.
Dòng tiếp theo: Số nguyên m (1 ≤ m ≤ 100) - số cặp trong dictionary B. m dòng tiếp theo: Tương tự như A.
Đầu ra:
In ra dictionary kết quả theo định dạng: mỗi dòng là một cặp khóa-giá trị, sắp xếp theo thứ tự từ điển của khóa. Khóa và giá trị cách nhau bởi dấu cách.

Ví dụ:
Đầu vào:
3
apple 5
banana 3
cherry 7
2
banana 2
date 4

Đầu ra:
apple 5
banana 5
cherry 7
date 4

Giải thích:
apple chỉ có trong A → giữ 5.
banana có trong cả A (3) và B (2) → tổng 5.
cherry chỉ có trong A → giữ 7.
date chỉ có trong B → giữ 4.
Lưu ý: Đầu ra trong test cases sử dụng văn bản không dấu để tránh lỗi kỹ thuật."""

data1 = {}
data2 = {}

n = int(input())
for _ in range(n):
    a, b = input().split()
    v1 = int(b)
    data1[a] = v1

m = int(input())
for _ in range(m):
    c, d = input().split()
    v2 = int(d)
    data2[c] = v2
    
result = data1.copy()

for k, v in data2.items():
    result[k] = result.get(k, 0) + v

for k, v in sorted(result.items()):
    print(k, v)