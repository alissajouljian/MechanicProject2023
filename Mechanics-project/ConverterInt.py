from Converter import Converter
from Spring import Spring


class UnitSpring:
    def __init__(self, spring_const=1):
        self.spring_const = spring_const

    def potential_energy(self, displac):
        return 0.5 * self.spring_const * displac ** 2


class ConverterInt(Converter):
    def __init__(self):
        self.spring = UnitSpring()

    def binary_to_decimal(self, binary):
        return int(binary, 2)

    def bits_to_springs(self, bits):
        binary_len = len(bits)
        s = [UnitSpring() for _ in range(binary_len)]
        for i in range(binary_len):
            if bits[binary_len - 1 - i] == '1':
                s[i] = self.spring
        return s
