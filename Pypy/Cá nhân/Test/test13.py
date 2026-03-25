balance = 50000000
while True:
    print("--- Bank ---")
    print("1. Rút tiền")
    print("2. Xem số dư")
    print("0. Thoát")
    choice = int(input("Chọn chức năng: "))
    if choice == 1:
        amount = int(input("Nhập số tiền cần rút: "))
        if amount <= 0:
            print("Số tiền không hợp lệ.")
        elif amount % 50000 != 0:
            print("Số tiền phải là bội số của 50,000.")
        elif amount > balance:
            print("Số dư không đủ.")
        else:
            balance -= amount
            print("Rút tiền thành công.")
            print("Số dư còn lại:", balance)
    elif choice == 2:
        print("Số dư hiện tại:", balance)
    elif choice == 0:
        print("Cảm ơn bạn đã sử dụng dịch vụ.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
