# Script kode program mencari data dengan menginput NIM
# Modifikasi kode program Latihan no. 2

openFile = open('d:/Latihan no. 2.txt', 'r')
readFile = openFile.readlines()

NIM = input('Masukkan NIM yang mau dicari : ')

for x in range(len(readFile)):

    Mahasiswa = readFile[x]
    A,B,C = Mahasiswa.split('|')

    if A == NIM:
        status = 'Ada'
        print('Data Mahasiswa')
        print('NIM     : ' + A)
        print('Nama    : ' + B)
        print('Alamat  : ' + C)
        break
    else:
        status = 'Tidak ada'

if status == 'Tidak ada':
    print('Data Mahasiswa tidak ditemukan')

openFile.close()