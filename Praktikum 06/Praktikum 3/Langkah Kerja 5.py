from operation import *

a = 2+4
b = 6-4
c = 4+7
d = 6-9
e = (10+2)/(7+5)
f = (12-34)

# Soal A
print(2, '+', 4, '*', 6, '-', 4, '=', kali(a, b))

# Soal B
print((4, '+', 7), '*', (6, '-', 9), '=', kali(c, d))

# Soal C
print((10, '+', 2), '/', (7, '+', 5), '/', (12, '-', 34), '=', bagi(e, f))
