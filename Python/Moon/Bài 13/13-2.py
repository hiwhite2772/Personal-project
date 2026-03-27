#1
import os
path = "test.txt"
if os.path.isfile(path):
    f = open(path)
    s = f.read()  #read()
    print(s)
    f.close()
else:
    print("Tệp tin không tồn tại!")

import os
path = "test.txt"
if os.path.isfile(path):
    f = open(path)
    while True:
        line = f.readline()  #readline()
        if (line == ""):
            break
        print(line, end="")
    print()
    f.close()
else:
    print("Tệp tin không tồn tại.")

import os
path = "test.txt"
if os.path.isfile(path):
    f = open(path)
    lines = f.readlines()  #readlines()
    print(lines)
    f.close()
else:
    print("Tệp tin không tồn tại!")

#2
with open("note.txt", "a+") as f:
    while True:
        line = input("Nhập nội dung: ")
        if (line.lower() == "exit"):
            break
        f.write(line + "\n")