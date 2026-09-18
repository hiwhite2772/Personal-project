thickness = int(input())
x = thickness * "H"

for i in range(1, thickness + 1):
    print(("H" * (2 * i - 1)).center(2*thickness-1))

for _ in range(thickness+1):
    print(" "*(thickness // 2) + x + " " * (3 * thickness) + x)

for _ in range(0, thickness, 2):
    print(" "*(thickness // 2) + "H" * (5 * thickness))

for _ in range(thickness+1):
    print(" "*(thickness // 2) + x + " " * (3 * thickness) + x)

for i in range(thickness, 0, -1):
    print(("H" * (2 * i - 1)).rjust(5*thickness + i - 1))