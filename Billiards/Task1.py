import numpy as np


def simulate_billiard(n):

    x0 = np.random.uniform(-1, 1)
    y0 = np.random.uniform(-1, 1)
    px0 = np.random.uniform(-1, 1)
    py0 = np.random.uniform(-1, 1)
    p_norm = np.sqrt(px0**2 + py0**2)
    px0 /= p_norm
    py0 /= p_norm
    reflections = np.zeros((n, 2))
 
    for i in range(n):
        a = px0**2 + py0**2
        b = 2 * (x0*px0 + y0*py0)
        c = x0**2 + y0**2 - 1
        t = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
        x = x0 + t * px0
        y = y0 + t * py0
        reflections[i] = [x, y]
      
        nx = x
        ny = y
        px = (ny**2 - nx**2) * px0 - 2 * nx * ny * py0
        py = -2 * nx * ny * px0 + (nx**2 - ny**2) * py0
        p_norm = np.sqrt(px ** 2 + py ** 2)
        px /= p_norm
        py /= p_norm
        x0 = x
        y0 = y
        px0 = px
        py0 = py
    return reflections
n = 5
print(simulate_billiard(n))
