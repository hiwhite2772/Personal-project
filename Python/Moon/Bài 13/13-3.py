#Xoá tệp tin
import os
try:
    os.remove("note1.txt")
except FileNotFoundError:
    print("File không tồn tại!")
except Exception as e:
    print("Có lỗi xảy ra", e)