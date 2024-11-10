import matplotlib.pyplot as plt
import numpy as np

mean = float(input("Enter mean: "))
sd = float(input("Enter standard deviation: "))
n = int(input("Enter number of samples: "))

random_numbers = np.random.normal(mean, sd, n)
# random_numbers = np.random.normal(10, 1, 100)

plt.hist(random_numbers, bins = 20, color = 'b', density = True)

# create an array with 100 equally spaces points between (mean - 3*sd) and (mean + 3*sd).
# This range ensures that the Gaussian probability density function is plotted over a reasonable interval.
x = np.linspace(mean - 3*sd, mean + 3*sd, 100)

# apply formula
plt.plot(x, 1 / (sd * np.sqrt(2 * np.pi)) * np.exp(-(x - mean) ** 2 / (2 * sd ** 2)), color = 'r')

plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Gaussian Distribution Curve")
plt.show()