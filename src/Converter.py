from abc import ABC, abstractmethod
import numpy as np
from Spring import Spring
from typing import List
from Body import Body


class Converter(ABC):

    def compute_oscillations(self, bits: str, t: float, dt: float, x0: float, vo: float) -> List[float]:
        body = Body(1, self.bits_to_springs(bits))
        return body.move(t, dt, x0, vo)

    def calculate_frequency_a(self, bits: List[int]):
        springs = self.bits_to_springs(bits)
        oscillations = Body(1, springs).move(10, 0.01, 0, 0)
        freqs, a = np.fft.fftfreq(len(oscillations), 0.01)[:len(oscillations) // 2], 2.0 / len(oscillations) * np.abs(np.fft.fft(oscillations)[:len(oscillations) // 2])
        return freqs, a

    def evaluate_decimal_value(self, bits: List[int]):
        freqs, a = self.calculate_frequency_a(bits)
        return np.sum(a * freqs)
    
    @abstractmethod
    def binary_to_decimal(self, binary):
        pass
    @abstractmethod
    def bits_to_springs(self, bits):
        pass
