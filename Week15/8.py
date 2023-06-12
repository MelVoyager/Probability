import numpy as np

def generate_drift_brownian_motion(T, N, mu, sigma, n):
    """
    Generate n paths of a drift brownian motion.
    
    Parameters:
    T: total time
    N: number of time steps
    n: number of paths
    mu: drift term
    sigma: standard deviation of the random term
    
    Returns:
    B: a (n, N+1) array of n paths of the brownian motion
    """
    dt = T/N
    # Initialize the brownian motion
    B = np.zeros((n, N+1))
    # Generate the brownian motion
    for i in range(n):
        B[i, 1:] = mu * dt + sigma * np.sqrt(dt) * np.random.standard_normal(size=N)
    return np.cumsum(B, axis=1)

# Test the function
B = generate_drift_brownian_motion(T=50, N=500, mu=1, sigma=1, n=1)

# Plot the result
import matplotlib.pyplot as plt
for i in range(B.shape[0]):
    plt.plot(np.linspace(0, 1, 501), B[i])
plt.savefig('8.png')
plt.show()
