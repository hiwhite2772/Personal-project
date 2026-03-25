list_a = [1,2,3]
list_b = list_a

list_b.append(4)
print("list_a sau khi thay đổi list_b:", list_a)
print("list_b:", list_b)
# => Cả list_a và list_b đều bị thay đổi vì chúng tham chiếu cùng một list

list_c = list_a.copy() 
list_c.append(5)
print("list_a sau khi thay đổi list_c:", list_a)
print("list_c:", list_c)
# => list_a không bị thay đổi lần này vì list_c là bản sao riêng biệt
