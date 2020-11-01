# Modifikasi kedua script bilangan bulat ganjil dari 0 hingga 100

banyak = 0
jumlah = 0
for bil in range (0, 100):
    bilGanjil = bil + 1
    if bilGanjil %2 == 1:
        banyak = banyak + 1
        jumlah = jumlah + bilGanjil
        print(bilGanjil)

print('Banyaknya bilangan ganjil : ' + str(banyak))
print('Jumlah seluruh bilangan   : ' + str(jumlah))
