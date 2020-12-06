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



