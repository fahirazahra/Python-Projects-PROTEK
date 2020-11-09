def faktorial(n):
    faktorial=1
    while(n > 0):
        faktorial=faktorial*n
        n -= 1
    return faktorial

def kombinasi(a, b):
    c = a - b
    kombinasi = faktorial(a)/faktorial(b)*faktorial(c)
    print(kombinasi)

def permutasi(a, b):
    c = a - b
    permutasi = faktorial(a)/faktorial(c)
    print(permutasi)



# Soal 3A
# C(5, 3)
a = 5
b = 3
kombinasi(a, b)

# Soal 3B
# P(10, 7)
a = 10
b = 7
permutasi(a, b)
    
