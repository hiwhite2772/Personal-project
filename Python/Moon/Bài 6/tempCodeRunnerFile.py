#Tính tổng các số 1 đến n
n = int(input("n = "))
if (n < 1):
  print("Không hợp lệ")
else:
  t = 0
  for i in range (1, n):
     t += i
  print("Tổng = ", t)