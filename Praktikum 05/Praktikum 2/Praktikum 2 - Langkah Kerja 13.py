# Modifikasi script perulangan angka dari 0 hingga 10

from random import randint
banyak = 0
while True:
    bil = randint(0, 10)
    print(bil)
    banyak = banyak + 1
    if bil == 5:
        break

print('Jumlah Perulangan : ' + str(banyak))
