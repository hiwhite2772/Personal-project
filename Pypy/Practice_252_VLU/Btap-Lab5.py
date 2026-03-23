#1
def tinh_tong_danh_sach():
    try:
        s = list(map(int, input("Nhập số phải có dấu ',': ").split(",")))
        print(sum(s))
    except:
        print("Lỗi! Vui lòng nhập chuỗi số!")
tinh_tong_danh_sach()

def tinh_tong_danh_sach2():
    try:
        nhapchuoiso = "1, 2, 3, 4, 5"
        danhsach = [int(i.strip()) for i in nhapchuoiso.split(",")]
        #Thực hiện tính tổng
        tong = 0
        for j in danhsach:
            tong += j
        print(tong)
    except:
        print("Lỗi! Vui lòng nhập chuỗi số!")
tinh_tong_danh_sach2()

#2
def kiem_tra_chia_het():
    try:
        a = int(input("Nhập a = "))
        b = int(input("Nhập b = "))
        print(f"{a} chia hết cho {b} là", a / b)
    except:
        print("Lỗi: Không thể chia cho 0! Vui lòng nhập b khác 0!")
kiem_tra_chia_het()

def kiem_tra_chia_het2():
    try:
        a = int(input("Nhập a = "))
    except:
        print("Vui lòng nhập số!")
    try:
        b = int(input("Nhập b = "))
    except:
        print("Vui lòng nhập số!")
    try:
        if a == 0 or b == 0:
            print("a hoặc b = 0, không thể chia.")
        else:
            chia = a / b
            print(chia)
    except:
        print("Lỗi: Phép tính chưa thực hiện")
kiem_tra_chia_het2()

#3
def tinh_trung_binh(danh_sach):
    if not danh_sach:
        print("Lỗi: Danh sách rỗng!")
        return
    for phan_tu in danh_sach:
        if not isinstance(phan_tu, (int, float)):
            print("Lỗi: Danh sách chứa giá trị không hợp lệ!")
            return
    diem_trung_binh = sum(danh_sach) / len(danh_sach)
    print(f"Điểm trung bình: {diem_trung_binh:.2f}")
tinh_trung_binh([8.8, 8.75, 10])

#4
def may_tinh_mini():
    try:
        a = int(input("Nhập a = "))
        b = int(input("Nhập b = "))
        o = input("Nhập sử dụng phép toán (+,-,*,/): ")

        if o == "+":
            kq = a + b
        elif o == "-":
            kq = a - b
        elif o == "*":
            kq = a * b
        elif o == "/":
            kq = a / b
        else:
            print("Lỗi: Phép toán không hợp lệ!")
            return

        print("Kết quả:", kq)

    except ValueError:

        print("Lỗi: Nhập sai kiểu dữ liệu!")
    except ZeroDivisionError:

        print("Lỗi: Không thể chia cho 0!")
may_tinh_mini()

#5
def demo_zero_division():
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

def demo_type_error():
    try:
        x = "abc" + 123
    except TypeError as e:
        print("TypeError:", e)

def demo_value_error():
    try:
        x = int("abc")
    except ValueError as e:
        print("ValueError:", e)

def demo_index_error():
    try:
        lst = [1, 2, 3]
        x = lst[5]
    except IndexError as e:
        print("IndexError:", e)

def demo_key_error():
    try:
        d = {"a": 1}
        x = d["b"]
    except KeyError as e:
        print("KeyError:", e)

def demo_attribute_error():
    try:
        x = 10
        x.append(5)
    except AttributeError as e:
        print("AttributeError:", e)

def demo_file_not_found():
    try:
        with open("khong_ton_tai.txt") as f:
            f.read()
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)

def demo_import_error():
    try:
        import module_khong_ton_tai
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError:", e)

def demo_name_error():
    try:
        print(abc)
    except NameError as e:
        print("NameError:", e)

def demo_assertion_error():
    try:
        x = 5
        assert x > 10, "x phải lớn hơn 10"
    except AssertionError as e:
        print("AssertionError:", e)

if __name__ == "__main__":
    demo_zero_division()
    demo_type_error()
    demo_value_error()
    demo_index_error()
    demo_key_error()
    demo_attribute_error()
    demo_file_not_found()
    demo_import_error()
    demo_name_error()
    demo_assertion_error()