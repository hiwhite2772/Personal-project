#Điền tên
name = input("Nhập tên của bạn: ")

#Nếu điền trống thì cảnh báo
while name == "":
    print("Không hợp lệ! Vui lòng nhập lại.")
    name = input("Nhập tên của bạn: ")
    
while True:
    age_input = input("Nhập tuổi năm trước của bạn: ")  #Điền tuổi

    if age_input.isdigit():  #Nếu kiểm tra số thì coi số tuổi đó
        age = int(age_input)

        if (0 <= age <= 120):  #Nếu số tuổi theo từ 0 đến 120 thì có thể dừng lại
            break

    print("Không hợp lệ! Vui lòng nhập lại.")  #Nếu điền trống hoặc số tuổi ko theo từ 0 đến 120 thì có thể cảnh báo

print(f"Chào bạn {name}, bạn đang {age + 1} tuổi năm nay!")  #Kết quả theo đủ điều kiện