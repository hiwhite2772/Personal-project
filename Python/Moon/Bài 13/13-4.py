# #Thực hành
# #1
# with open("my_file.txt", "r") as f:
#     content = f.read()
#     if len(content) == 0:
#         print("Tệp tin rỗng")
#     else:
#         print(content)

# #2
# import os
# path = ""
# file_name = input("Nhập tên: ")
# path = os.path.join(path, file_name + ".txt")
# print(path)
# if (len(file_name) == 0):
#     print("Tên tệp không được trống!")
#     exit()
# else:
#     with open(path, "w+", encoding="utf-8") as file:
#         file.write("Python cho người mới bắt đầu.")

# #3
# from calculator import Calculator

# def save_history(s):
#     with open("result.txt", "a+") as f:
#         f.write(s + "\n")

# def main():
#     cal = Calculator()
#     while True:
#         print("=====================")
#         print("Chương trình máy tính")
#         print("1. Cộng")
#         print("2. Trừ")
#         print("3. Nhân")
#         print("4. Chia")
#         print("0. Thoát")
#         print("=====================")
#         try:
#             choice = int(input("Nhập lựa chọn: "))
#             if (choice < 0) or (choice > 4):
#                 print("Lựa chọn không hợp lệ.")
#                 continue
#             if choice == 0:
#                 print("Đã thoát chương trình")
#                 break
#             a = int(input("Nhập a = "))
#             b = int(input("Nhập b = "))
#         except:
#             print("Vui lòng nhập số!")
#             continue
#         if choice == 1:
#             t = cal.tong(a, b)
#             save_history(f"{a} + {b} = {t}")
#         if choice == 2:
#             t = cal.hieu(a, b)
#             save_history(f"{a} - {b} = {t}")
#         if choice == 3:
#             t = cal.tich(a, b)
#             save_history(f"{a} x {b} = {t}")
#         if choice == 4:
#             t = cal.thuong(a, b)
#             if t == None:
#                 continue
#             save_history(f"{a} : {b} = {t}")
#         print(f"Kết quả: {t}")
# if __name__ == "__main__":
#     main()

#4
from document import normalize_text
from rw_file import readFile, writeFile
def main():
    try:
        content = readFile("text.txt")
        if len(content) == 0:
            print("Tệp tin vẫn trống rỗng!")
        else:
            normalize_content = normalize_text(content)
            writeFile("result2.txt", normalize_content)
            print("Đã chuẩn hoá văn bản.")
    except FileNotFoundError:
        print("Tệp tin không tìm thấy!")
        return
if __name__ == "__main__":
    main()