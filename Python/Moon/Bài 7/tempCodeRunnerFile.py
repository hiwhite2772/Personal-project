#Câu 3
s = input("Nhập số nguyên: ")
l = None
if (s != ""):
    l = list(map(int, s.split(",")))
else:
    l = list()

t = 0
for i in l:
    t += i
print(t)

#Câu 4
l = ['a', 'b', 'c']
t = 0
for i in l:
    if( ( type(i) == int or type(i) == float) and i > 0):
        t += i
if t == 0:
    t = -1
print(t)

#Câu 5
m = input("l = ").split(",")
l = list()
for i in m:
    if (i.isnumeric()):
        l.append(int(i))
    elif (i.isdecimal()):
        l.append(float(i))
    else:
        l.append(i)

n = input("t = ").split(";")
t = list()
for i in n:
    if (i.isnumeric()):
        t.append(int(i))
    elif (i.isdecimal()):
        t.append(float(i))
    else:
        t.append(i)
t = tuple(t)

rs=l.copy()
rs.extend(t)
print(rs)