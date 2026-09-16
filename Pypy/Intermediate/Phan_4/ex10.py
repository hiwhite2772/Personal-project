"""Bạn cần tạo một lớp Book để quản lý thông tin sách trong thư viện. 
Lớp Book cần có các thuộc tính: title (tiêu đề), author (tác giả), year (năm xuất bản). 
Cần có phương thức str để trả về chuỗi mô tả sách theo định dạng (dùng chữ KHÔNG DẤU): 
“Tieu de: [title], Tac gia: [author], Nam: [year]”.
Chương trình sẽ đọc từ input: dòng đầu tiên là số nguyên n (1 ≤ n ≤ 10) - số lượng sách. 
n dòng tiếp theo, mỗi dòng chứa thông tin một sách gồm nhiều từ cách nhau bởi dấu cách, theo quy tắc: 
từ cuối cùng là year (năm), từ ngay trước year là author (tác giả), toàn bộ phần còn lại ở đầu dòng là title (tiêu đề - có thể gồm nhiều từ).
Xuất ra: Với mỗi sách, in ra một dòng mô tả sách theo định dạng trên.

Ví dụ:
Input:
2
Toan hoc Nguyen Van A 2020
Van hoc Tran Thi B 2019
Output:
Tieu de: Toan hoc Nguyen Van, Tac gia: A, Nam: 2020
Tieu de: Van hoc Tran Thi, Tac gia: B, Nam: 2019

Lưu ý: Toàn bộ output sử dụng văn bản KHÔNG DẤU (Tieu de / Tac gia / Nam) để tránh lỗi kỹ thuật."""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Tieu de: {self.title}, Tac gia: {self.author}, Nam: {self.year}"
t = int(input())
for _ in range(t):
    td, ten, nam = input().strip().rsplit(maxsplit=2)
    b = Book(td, ten, nam)
    print(b)