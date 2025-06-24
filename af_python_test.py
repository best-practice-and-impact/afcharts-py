import matplotlib.pyplot as plt
import numpy as np

# Import the stylesheet used
plt.style.use('.images/af_test.mplstyle')

print(plt.style.available)


# Generate arbitrary data
np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + np.random.normal(scale=0.1, size=50)

# Create scatter plot
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

plt.show()