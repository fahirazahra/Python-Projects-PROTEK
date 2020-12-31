# Script kode program memasukkan inputan data ke file.txt

openFile = open('d:/Latihan no. 2.txt', 'w')

while True:
    
    NIM = input('Masukkan NIM               : ')
    Nama = input('Masukkan Nama Mahasiswa    : ')
    Alamat = input('Masukkan Alamat            : ')

    result = (NIM + '|' + Nama + '|' + Alamat)
    openFile.write(result + '\n')

    print()
    repeat = input('Ulangi input lagi (yes/no) : ')
    print()

    if repeat == 'yes':
        continue
    elif repeat == 'no':
        break
    else:
        print('INVALID INPUT')
        continue

openFile.close()