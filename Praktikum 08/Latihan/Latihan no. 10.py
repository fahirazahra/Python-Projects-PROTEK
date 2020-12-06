# Modifikasi script Latihan no. 7-9
# Script menghitung total harga buah yang dibeli (sesuai kemauan)


nama_harga = {'Apel' : 5000,
              'Jeruk' : 8500,
              'Mangga' : 7800,
              'Duku' : 6500}


namaBuah = list(nama_harga)
hargaBuah = list(nama_harga.values())
totalBuah = []

while True:
    beli = input('Nama buah yang dibeli             : ')
    banyak = int(input('Berapa Kg                         : '))
    harga = namaBuah.index(beli)
    total = (hargaBuah[harga]*banyak)
    totalBuah.append(total)
    beliLagi = input('Beli buah yang lain? (yes/no)     : ')
    if beliLagi == 'no':
        break
    else:
        continue

totalHarga = sum(totalBuah)

print('------------------------------------------------')
print('Total harga                       : ', totalHarga)


