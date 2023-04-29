from Converter8Bit import Converter8Bit
from ConverterInt import ConverterInt
from ConverterFloat import ConverterFloat





# Converter8Bit
converter8bit = Converter8Bit() 
decimal_val = converter8bit.binary_to_decimal('00100000')
springs = converter8bit.bits_to_springs('00100000')
print("Converter8Bit:")
print(f"Length of springs: {len(springs)}")
print(f"Decimal value of sequence '00100000': {decimal_val}\n")



# ConverterInt
converterint = ConverterInt()
decimal_val = converterint.binary_to_decimal('11110000')
springs = converterint.bits_to_springs('11110000')
print("ConverterInt:")
print(f"Length of springs: {len(springs)}")
print(f"Decimal value of sequence '11110000': {decimal_val}\n")




# ConverterFloat
converterfloat = ConverterFloat(4,4)
decimal = converterfloat.binary_to_decimal("1100.11")
springs = converterfloat.bits_to_springs("1100.11")
print("ConverterFloat:")
print(f"Binary representation: {1100.11}")
print(f"Decimal value: {decimal}")
print(f"Unit springs: {len(springs)}")
