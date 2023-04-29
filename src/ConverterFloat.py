from Converter import Converter
from ConverterInt import ConverterInt


class ConverterFloat(Converter):

    def __init__(self, integer_bits, fraction_bits):
        super().__init__()
        self.integer_bits = integer_bits
        self.fraction_bits = fraction_bits
        self.integer_converter = ConverterInt()
        self.fraction_converter = ConverterInt()
        
    def binary_to_decimal(self, binary):
            point = binary.find('.')
            if (point == -1):
                point = len(binary)
            intD = 0
            fracD = 0
            
            twos = 1
            for i in range(point - 1, -1, -1):
                intD += ((ord(binary[i]) - ord('0')) * twos)
                twos *= 2
    
            twos = 2
            for i in range(point + 1, len(binary)):
                fracD+= ((ord(binary[i]) - ord('0')) / twos)
                twos *= 2.0
            ans = intD + fracD
    
            return ans


    def bits_to_springs(self, bits):
        integer_springs = self.integer_converter.bits_to_springs(bits[:self.integer_bits])
        fraction_springs = self.fraction_converter.bits_to_springs(bits[self.integer_bits:])
        return integer_springs + fraction_springs
