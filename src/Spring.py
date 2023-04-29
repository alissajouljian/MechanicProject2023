import numpy as np

class Spring:
    def __init__(self, k=1.0):
        self.k = k

    def move(self, t0, t1, dt, x0, v0=0.0, m=1.0):
        w = np.sqrt(self.k / m)
        t = np.arange(t0, t1, dt)
        x = x0 * np.cos(w * t) + (v0 / w) * np.sin(w * t)
        return x

    def force(self, x):
        return -self.k * x

    def potential_energy(self, x):
        return 0.5 * self.k * x ** 2

    def get_stiffness(self):
        return self.k

    def set_stiffness(self, k):
        self.k = k

    def in_series(self, that):
        return Spring(self.k + that.get_stiffness())

    def in_parallel(self, that):
        return Spring(1.0 / (1.0 / self.k + 1.0 / that.get_stiffness()))
