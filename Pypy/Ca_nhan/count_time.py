import time
mytime = int(input("Nhập số giây đếm ngược: "))
for x in reversed(range(0, mytime + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Merry Christmas!")

mytime2 = int(input("Nhập số giây đếm ngược tiếp theo: "))
for x in reversed(range(0, mytime2 + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Happy new year!")