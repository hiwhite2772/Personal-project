#Kết thúc dòng bằng dấu chấm và xuống dòng 
s1 = "Người giải code rất thông minh và học giỏi mọi ngôn ngữ"
s2 = "Dân học IT có tiến bộ dần phát triển"
print(s1, end=".\n")
print(s2, end=".\n")

#Nhập số tiền giá trị
so_tien = int(input("Nhập số tiền: "))
print("Số tiền là: {:,.0f}VND".format(so_tien))