from math import isqrt
​
def find_next_square(sq):
    root = int(sq**0.5)
​
    if root**2!=sq:
        return -1
​
    return (root+1)**2