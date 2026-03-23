#Xử lý ngoại lệ - exception
#1
try:
    a = int(input("a = "))
    b = int(input("b = "))
    result = a / b
    print(f"{a} chia {b} bằng {result}")
except ValueError:
    print("Lỗi: Không phải số nguyên")
except ZeroDivisionError:
    print("Lỗi: Chia cho số 0")
except Exception as e:
    print("Lỗi không xác định:", e)

#2
dictionary = {
    "apple":"quả táo",
    "kiwi":"quả kiwi",
    "mango":"quả xoài",
    "banana":"quả chuối",
    "cherry":"quả anh đào",
    "watermelon":"quả dưa hấu",
    "pineapple":"quả dứa"
}

try:
    word = input("Nhập từ khoá của tiếng anh: ").lower()
    meaning = dictionary[word]
    print(f"Nghĩa của từ '{word}' là '{meaning}'")
except KeyError:
    print(f"Từ {word} không có trong từ điển")

#3
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90 ,100]
try:
    my_index = int(input())
    my_value = my_list[my_index]
    print(f"Giá trị của phần tử có chỉ số {my_index} là {my_value}")
except ValueError:
    print("Lỗi: vui lòng nhập 1 số nguyên.")
except IndexError:
    print(f"Lỗi: Chỉ số {my_index} không hợp lệ.")