import math

import numpy as np
from typing import List


class FT:
    def __init__(self, x):
        self.N = len(x)
        self.real = np.zeros(self.N)
        self.imag = np.zeros(self.N)

        for k in range(self.N):  
            for n in range(self.N):  
                self.real[k] += x[n] * np.cos((2 * np.pi * k * n / self.N))
                self.imag[k] -= x[n] * np.sin((2 * np.pi * k * n / self.N))

    def get_spectrum(self):
        return np.sqrt(self.real **2 +self.imag ** 2)

    def get_phase(self):
        return np.arctan2(self.imag, self.real)

    def get_frequency(self, k):
        return (k / self.N)

    def fourier_transform(self, x):
        N = len(x)
        a = []
        for i in range(N):
            ak = 0.0
            for n in range(N):
                ak += x[n] * math.sin(2 * math.pi * i * n / N)
            ak /= N / 2.0
            a.append(ak)
        return a
