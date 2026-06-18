from collections import deque
q = deque()

q.append('Data Science')
q.append('Data Structures and Algorithms')
q.append('Learning Data Analytics')
q.append('Big Data')

print(q)
print(q.popleft())
print(q.popleft())
print(q)