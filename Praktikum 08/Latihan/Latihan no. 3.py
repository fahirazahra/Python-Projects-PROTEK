# Script menghitung karakter huruf dari inputan nama mahasiswa

namaMahasiswa = []

while True:
    try:
        inputNama = str(input('Masukkan Nama                      : '))
        namaMahasiswa.append(inputNama)
        ulangLagi = input('Ingin masukkan nama lagi? (yes/no) : ')
        if ulangLagi == 'yes':
            True
        else:
            break
    except ValueError:
        print('Data yang anda input bukan tipe string')
        
namaMahasiswa.sort()

print('-----------------------------------------------------')

print('Jumlah karakter huruf : ')

for inputNama in range(len(namaMahasiswa)):
    print(namaMahasiswa[inputNama],'(',len(namaMahasiswa[inputNama]),'karakter)')
