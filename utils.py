import numpy as np

def generate_random_sales(min_val, max_val, size):
    """Generate random sales data between min_val and max_val"""
    return np.random.randint(min_val, max_val + 1, size=size)
