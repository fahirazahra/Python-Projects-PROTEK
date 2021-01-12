# Script kode program menginput data peminjam buku di perpustakaan

from datetime import *
import os

writeData = open('Latihan2.txt', 'w')

while True:
    Kode = input('Masukkan Kode Member : ')
    Nama = input('Masukkan Nama Member : ')
    Judul = input('Masukkan Judul Buku  : ')
    TglPinjam = date.today()
    TglKembali = (TglPinjam + timedelta(days = 7))
    
    listData = [Kode, Nama, Judul, str(TglPinjam), str(TglKembali), '\n']
    writeData.write('|'.join(listData))

    print()
    repeat = input('Ulangi lagi (yes/no) : ')
    print()

    if repeat == 'yes':
        continue
    elif repeat == 'no':
        break
    else:
        print('INVALID INPUT')

writeData.close()