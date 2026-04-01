#9
file = open("numbers.txt", "w")
for i in range(1, 11):
    file.write(str(i)+"\n")
file.close()
#10
s = 0
file = open("numbers.txt", "r")
for line in file:
    s += int(line)
print(s)
file.close()
#11
def add_name():
    name = input()
    with open("names.txt", "a") as file:
        file.write(name + "\n")
    print("Saved!")
def view_name():
    try:
        with open("names.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Chưa dữ liệu!")
while True:
    print("\n1. Add name")
    print("2. View name")
    print("3. Exit")

    choice = input()
    if choice == "1":
        add_name()
    elif choice == "2":
        view_name()
    elif choice == "3":
        print("Exited!")
        break
    else:
        print("Không hợp lệ!")