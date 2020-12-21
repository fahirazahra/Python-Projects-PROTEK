# Script kode program mengacak string menggunakan perintah random.sample()

def shuffleString(x, n):
    import random
    hasil = []

    for j in range(n):
        acakString = [''.join(random.sample(x, len(x)))]
        hasil.append(acakString)
        print(acakString)
    return hasil

# Jika n = 2
shuffleString('aku', 2)

# Jika n = 3
shuffleString('aku', 3)

# Jika n = 4
shuffleString('aku', 4)