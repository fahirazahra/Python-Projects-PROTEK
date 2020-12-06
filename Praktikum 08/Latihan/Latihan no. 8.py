# Latihan no. 7-9

nama_harga = {'Apel' : 5000,
              'Jeruk' : 8500,
              'Mangga' : 7800,
              'Duku' : 6500}


# Script menentukan harga buah yang paling mahal menggunakan function (Latihan no. 7)

def buahMahal(nama_harga):
    buah = list(nama_harga.keys())
    dataBuah = tuple(nama_harga.values())
    hargaTermahal = max(dataBuah)
    data = dataBuah.index(hargaTermahal)
    
    print('Buah yang paling mahal adalah',(buah[data]))
    
buahMahal(nama_harga)

print('=============================================')


# Script menentukan rata-rata harga satuan buah (Latihan no. 8)

def RerataHarga(nama_harga):
    RerataHarga = []
    for i in nama_harga:
        RataRata = list(nama_harga.values())
        Rata2 = (sum(RataRata)/len(RataRata))
        RerataHarga = [Rata2]
    return RerataHarga

print('Rata-rata harga satuan buah adalah',(RerataHarga(nama_harga)))



