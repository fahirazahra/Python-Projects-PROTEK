# Script menyimpan inputan data karyawan

from datetime import *
import os

writeData = open('dataKaryawan.dat', 'w')

def addKaryawan(NIP, Nama, Alamat, Golongan, TanggalLahir, Usia):
    listData = [NIP, Nama, Alamat, Golongan, TanggalLahir, str(Usia), '\n']
    writeData.write('|'.join(listData))

def getUsia(TanggalLahir):
    formatTglLahir = TanggalLahir.split('-')
    TahunLahir = int(formatTglLahir[0])
    Tahun2021 = datetime.now()
    Usia = (Tahun2021.year - TahunLahir)

    return Usia

while True:
    NIP = input('Masukkan NIP                          : ')
    Nama = input('Masukkan Nama                         : ')
    Alamat = input('Masukkan Alamat                       : ')
    Golongan = input('Masukkan Golongan (A/B/C)             : ')
    TanggalLahir = input('Masukkan Tanggal Lahir (YYYY-MM-DD)   : ')

    Usia = getUsia(TanggalLahir)

    print()
    repeat = input('Tambah Data (yes/no)                  : ')
    print()

    if repeat == 'yes':
        addKaryawan(NIP, Nama, Alamat, Golongan, TanggalLahir, Usia)
        continue
    elif repeat == 'no':
        addKaryawan(NIP, Nama, Alamat, Golongan, TanggalLahir, Usia)
        break
    else:
        print('INVALID INPUT')
        break

writeData.close()