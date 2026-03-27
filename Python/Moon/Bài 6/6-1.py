# In ra các số từ 1 đến 10 trên cùng một dòng, cách nhau bởi dấu tab
for i in range(1, 11):
 print (i, end="\t")

# In ra các kí tự từ 'a' đến 'z' trên cùng một dòng, cách nhau bởi dấu tab
s = input("Nhập xâu kí tự: ")
for c in s:
    print(c, end="\t")
    
#Tính tổng các số 1 đến n
n = int(input("n = "))
if (n < 1):
  print("Không hợp lệ")
else:
  t = 0
  for i in range (1, n):
     t += i
  print("Tổng = ", t)