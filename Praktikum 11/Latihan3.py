# Script kode program data peminjaman buku di perpustakaan

from datetime import *
import Latihan1

openFile = open('Latihan2.txt', 'r')
readFile = openFile.readlines()

print('='*100)
Kode = input('Masukkan Kode Member         : ')
print()

for y in range(len(readFile)):
    if Kode in readFile[y]:
        formatDate = readFile[y].split('|')
        Status = 'Ada'
        break
    else:
        Status = 'Tidak ada'
        continue

if Status == 'Ada':
    print('DATA PEMINJAMAN BUKU')
    print()
    print('Kode Member                  :', formatDate[0])
    print('Nama Member                  :', formatDate[1])
    print('Judul Buku                   :', formatDate[2])
    print('Tanggal Mulai Peminjaman     :', formatDate[3])
    print('Tanggal Maksimal Peminjaman  :', formatDate[4])
    print('Tanggal Pengembalian         :', datetime.date(datetime.now()))
    telatKembali = Latihan1.diffDate(formatDate[4])
    Denda = (abs(telatKembali)*2000)

    if telatKembali >= 0:
        print('Terlambat                    : 0 Hari')
        print('Denda                        : Rp. 0')
    else:
        print('Terlambat                    :', abs(telatKembali))
        print('Denda                        :', Denda)

else:
    print('INVALID DATA')