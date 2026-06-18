from queue import Queue
q = Queue(maxsize = 5)
print(q.qsize())
q.put("Data Analytics")
q.put("Big Data")
q.put("Learning Data Analytics")
print(q.qsize())
print(q.get())
print(q.get())