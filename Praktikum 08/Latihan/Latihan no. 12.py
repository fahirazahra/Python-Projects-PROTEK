# Modifikasi script Latihan no. 7-9
# Script menghitung total harga buah yang dibeli (sesuai kemauan)

# Modifikasi Latihan no. 10

nama_harga = {'Apel' : 5000,
              'Jeruk' : 8500,
              'Mangga' : 7800,
              'Duku' : 6500}

print('Menu :')
print('a. Tambah data buah')
print('b. Beli buah')
print('c. Hapus data buah')

namaBuah = list(nama_harga)
hargaBuah = list(nama_harga.values())
totalBuah = []

while True:
    pilihanMenu = input('Pilihan menu : ')
    beli = input('Nama buah yang dibeli             : ')
    banyak = int(input('Berapa Kg                         : '))
    harga = namaBuah.index(beli)
    total = (hargaBuah[harga]*banyak)
    totalBuah.append(total)
    beliLagi = input('Beli buah yang lain? (yes/no)     : ')
    if pilihanMenu == 'a':
        pilihanMenu
        if beli in nama_harga:
            beliBuah = input('Masukkan nama buah : ')
        hargaSatuan = int(input('Masukkan harga satuan : '))
        nama_harga[beli] = hargaSatuan
        print(nama_harga)
    elif pilihanMenu == 'c':
        hapusBuah = input('Buah apa yang mau dihapus? ')
        if hapusBuah not in nama_harga:
            hapusBuah = input('Masukkan nama buah : ')
        del nama_harga[hapusBuah]
        print(nama_harga)
    elif beliLagi == 'no':
        break
    else:
        continue
        

totalHarga = sum(totalBuah)

print('------------------------------------------------')
print('Total harga                       : ', totalHarga)


