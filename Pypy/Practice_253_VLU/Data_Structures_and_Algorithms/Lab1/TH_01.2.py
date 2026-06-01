def tuyen_tinh(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1

array = [15, 25, 80, 30, 60, 50,
         110, 100, 130, 180]
x = int(input("Nhap so nguyen: "))
result = tuyen_tinh(array, x)

if result != -1:
    print(f"Phan tu tim thay duoc tai vi tri la: {result}")
else:
    print("Phan tu khong duoc tim thay trong arr[]")
