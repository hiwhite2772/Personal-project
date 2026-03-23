class Library:
    def __init__(self, name, title, total_books):
        self.name = name
        self.title = title
        self.total_books = total_books
    def borrowBook(self, book):
        self.total_books -= book
        print(f"Đã mượn bộ sách: {book}")
    def returnBook(self, book):
        if book > self.total_books:
            print("Không đủ bộ quyển sách!")
        else:
            self.total_books += book
            print(f"Đã trả bộ sách: {book}")
    def showInfo(self):
        print(f"Tên: {self.name}")
        print(f"Tên tiêu đề: {self.title}")
        print(f"Hiện dư bộ quyển sách: {self.total_books}")
Account = Library("White", "Golden", 15)
Account.borrowBook(5)
Account.returnBook(6)
Account.showInfo()