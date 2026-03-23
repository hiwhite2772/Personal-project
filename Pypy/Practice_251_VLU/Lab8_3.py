numbers = [10,5,20,15,30,7,42,-5]
max_val = numbers[0]
#Giá trị lớn nhất của list
for num in numbers:
    if num > max_val:
        max_val = num
print("Giá trị lớn nhất:", max_val)
#Lẻ và chẵn của list
list_chan = []
list_le = []
for num in numbers:
    if num % 2 == 0:
        list_chan.append(num)
    else:
        list_le.append(num)
print("Danh sách các số chẵn:", list_chan)
print("Danh sách các số lẻ:", list_le)