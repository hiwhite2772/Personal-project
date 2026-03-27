import matplotlib.pyplot as plt
 
x = [1, 5, 8]
y = [2, 10, 4]

plt.plot([x[0], x[1]], [y[0], y[1]], marker='o')
plt.plot([x[1], x[2]], [y[1], y[2]], marker='o')
plt.plot([x[2], x[0]], [y[2], y[0]], marker='o')

plt.show()