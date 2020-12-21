# Script kode program memasukkan list biodata mahasiswa ke dalam tabel
# Dengan memisahkan bagian biodata serta mengurutkan format tanggal lahir terlebih dahulu menggunakan perintah split()

mahasiswa = ['K001:ROSIHAN ARI          :1979-09-01 :SOLO',
             'K002:DWI AMALIA FITRIANI  :1979-09-17 :KUDUS',
             'K003:FAZA FAUZAN          :2005-01-28 :KARANGANYAR']

print('='*70)
print('NIM'.ljust(10), 'Nama Mahasiswa'.ljust(15), 'Tanggal Lahir'.rjust(23), 'Tempat Lahir'.rjust(17))
print('-'*70)

listMahasiswa = []
for i in range(len(mahasiswa)):

    titik2 = mahasiswa[i].split(':')
    listMahasiswa.append(titik2)

    strip = listMahasiswa[i][2].split('-')
    strip.reverse()

    gantiStrip = '/'.join(strip)
    listMahasiswa[i][2] = gantiStrip

for j in range(len(listMahasiswa)):
    
    print(listMahasiswa[j][0].ljust(10),
          listMahasiswa[j][1].ljust(15),
          listMahasiswa[j][2].center(22),
          listMahasiswa[j][3].ljust(17))

print('-'*70)