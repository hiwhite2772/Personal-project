# Đề hỏi: mỗi dòng cách từng số mà không phải đọc 1 dòng các số cách nhau.
try:
    with open("input.txt", "r") as f:
        #Đây đọc mỗi dòng từng số đó.
        data = [int(line.strip()) for line in f]
        print(data)

    #Đếm số và tổng số đều là số lẻ
    count_odd = sum(1 for i in data if i % 2 != 0)
    total_odd = sum(i for i in data if i % 2 != 0)

    with open("output.txt", "w") as f:
        #Xuất ra file
        f.write(str(count_odd) + "\n")
        f.write(str(total_odd))

    with open("output.txt", "r") as f:
        #Xuất ra màn hình để kiểm tra
        print(f.read())

except FileNotFoundError:
    #Nếu file chưa tạo ra thì sẽ báo lỗi này!
    print("Không tìm thấy file!")