import matplotlib.pyplot as plt
import numpy as np

def gaussian_distribution(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))

mu = 0  
sigma = 1  

x_values = np.linspace(-5, 5, 500)
y_values = gaussian_distribution(x_values, mu, sigma)

plt.plot(x_values, y_values, label=f'$\mu={mu}$, $\sigma={sigma}$', color='blue')
plt.title("Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()
