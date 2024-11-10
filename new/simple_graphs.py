import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size = (5))
y = np.random.randint(100, size = (5))

# line graph
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Line Graph")

# bar plot
plt.subplot(2, 3, 2)
c = np.array(['A', 'B', 'C', 'D', 'E'])
a = np.array([5, 10, 15, 20, 25])
plt.bar(c, a)
plt.title("Bar Graph")

# scatter plot
plt.subplot(2, 3, 3)
plt.scatter(x, y)
plt.title('Scatter Plot')

# histogram
x2 = np.random.randint(100, size=(100))
plt.subplot(2, 3, 4)
plt.hist(x2)
plt.title("Histogram")

# pie chart
plt.subplot(2, 3, 5)
plt.pie(x, labels = c)
plt.legend(loc = 'upper right')
plt.title("Pie chart")

# stacked bar
plt.subplot(2, 3, 6)
c = np.array(['A', 'B', 'C', 'D', 'E'])
a = np.array([5, 10, 15, 20, 25])
b = np.array([10, 15, 20, 25, 30])
plt.bar(c, b)
plt.bar(c, a)
plt.title("Stacked Bar Graph")

plt.tight_layout()
plt.show()