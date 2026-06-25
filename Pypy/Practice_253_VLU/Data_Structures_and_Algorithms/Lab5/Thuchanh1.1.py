thislist = ["hanoi", "saigon", "danang", "nhatrang", "cantho"]
print(thislist)

thislist.insert(2, "cantho")
print(thislist)
thislist.insert(3, "Hue")
print(thislist)

thislist = ["hanoi", "saigon", "danang", "nhatrang", "cantho"]
thislist.pop(2)
print(thislist)

thislist = ["hanoi", "saigon", "danang", "nhatrang", "cantho"]
thislist.sort()
print(thislist)

thislist = [100, 15, 50, 65, 82, 23]
thislist.sort()
print(thislist)

list1 = ['data analytics', 'data science', 'data structures', 'algorithms', 2020, 2021]
list2 = [i for i in range(10)]
print(f"list1[1]: {list1[1]}")
print(f"list2[2:8]: {list2[2:8]}")