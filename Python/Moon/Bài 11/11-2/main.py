import my_module
a, b = map(int, input("Nhập số: ").split())
print(f"{a} + {b} = {my_module.cong(a, b)}")
print(f"{a} - {b} = {my_module.tru(a, b)}")
print(f"{a} * {b} = {my_module.nhan(a, b)}")
print(f"{a} / {b} = {my_module.chia(a, b)}")
