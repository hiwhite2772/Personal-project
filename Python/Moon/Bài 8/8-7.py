#Các phương thức trong dictionary
#VD1
student = {'name': 'Andy', 'age': 21, 'job': 'doctor'}
infor = student.copy()
print(infor)
#VD2
Me = {'name': 'H.I', 'age': 18, 'job': 'student'}
value = Me.setdefault('age', 0)
print(value)
value2 = Me.setdefault('address', 'HCM')
print(value2)
print(Me)