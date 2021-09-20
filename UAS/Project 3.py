# Script memindahkan data karyawan ke dalam tabel
# Modifikasi script kode program Project 1

readFile = open('dataKaryawan.dat', 'r')

dataKaryawan = [{'Kode Karyawan' : 'K001', 'Nama Karyawan' : 'ROSIHAN ARI', 'Alamat' : 'COLOMADU', 'Golongan' : 'C', 'Tanggal Lahir' : '1979-09-01', 'Usia' : '39'},
                {'Kode Karyawan' : 'K002', 'Nama Karyawan' : 'BUDIMAN',     'Alamat' : 'SEMARANG', 'Golongan' : 'A', 'Tanggal Lahir' : '1980-02-20', 'Usia' : '38'}]

print('-'*150)
print(('Kode Karyawan'.ljust(20, ' ')),
      ('Nama Karyawan'.ljust(20, ' ')),
      ('Alamat'.ljust(20, ' ')),
      ('Golongan'.ljust(20, ' ')),
      ('Gaji Pokok'.rjust(20, ' ')),
      ('Tanggal Lahir'.ljust(10, ' ')),
      ('Usia'.rjust(20, ' ')))
print('-'*150)

for listData in dataKaryawan:
    A = 'A'
    B = 'B'
    C = 'C'
    Golongan = 'Golongan'

    if Golongan == 'A':
       gajiPokok = 4000000
    elif Golongan == 'B':
        gajiPokok = 4500000
    elif Golongan == 'C':
        gajiPokok = 5000000
        
    print(str(listData['Kode Karyawan']).ljust(20, ' '),
          str(listData['Nama Karyawan']).ljust(20, ' '),
          str(listData['Alamat']).ljust(20, ' '),
          str(listData['Golongan']).ljust(20, ' '),
          str(listData['Tanggal Lahir']).ljust(10, ' '),
          str(listData['Usia']).rjust(20, ' '))

print('-'*150)