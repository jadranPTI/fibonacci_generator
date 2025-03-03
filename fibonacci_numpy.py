import numpy as np

def fibonacci_numpy(n):
    sqrt_5 = np.sqrt(5)
    phi = (1 + sqrt_5) / 2
    return int((phi**n - (-phi)**-n) / sqrt_5)
