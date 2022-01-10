# Напишите программу на Python, чтобы определить, выполняется ли оболочка Python в
# 32-битном или 64-битном режиме в ОС.

import struct
print(struct.calcsize("P") * 8)