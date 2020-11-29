# Script memanggil dan menambahkan data di file notepad dengan append

import time

namaFile = input('Masukkan nama file : ')
readFile = open(namaFile, 'r')
print(readFile.read())
readFile.close()
time.sleep(1)

try:
    appendFile = open(namaFile, 'a')
    
    while True:
        data = input('Data yang mau ditambahkan : ')
        appendFile.write(data)
        tambahData = str(input('Mau lagi? (yes/no) : '))
        if tambahData == 'yes':
            True
        else:
            break
    appendFile.close()
    
except FileNotFoundError:
    print('File tidak ditemukan/Nama file salah')
