from Converter import Converter
from Spring import Spring


class Converter8Bit(Converter):
    def binary_to_decimal(self, binary):
        return int(binary, 2)

    def bits_to_springs(self, bits):
        springs = []
        for bit in bits:
            if bit == '0':
                springs.append(Spring(1))
            else:
                springs.append(Spring(2))
        for i in range(len(springs)-1):
            if bits[0] == '0':
                springs[i+1] = Spring.in_series(springs[i], springs[i+1])
            else:
                springs[i+1] = Spring.in_parallel(springs[i], springs[i+1])
        return springs
