# Soal 2A

def starFormation1(n):
    for j in range (1, n+1):
        print('*'*j)

# Contoh 2A
starFormation1(4)
print()



# Soal 2B

def starFormation2(n):
    for j in range(1, n+1):
        print('*'*(n+1-j))

# Contoh 2B
starFormation2(4)
print()



# Soal 2C

def starFormationGabungan(n):
    starFormation1(n//2)
    starFormation2(n-n//2)

# Contoh 2C
starFormationGabungan(7)
