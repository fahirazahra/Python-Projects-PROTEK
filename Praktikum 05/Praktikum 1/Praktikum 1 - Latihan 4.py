# Script menghitung gaji karyawan

kodeKaryawan = input('Masukkan kode karyawan   : ')
namaKaryawan = input('Masukkan nama karyawan   : ')
golKaryawan = input('Masukkan golongan        : ')

print('===== ===== ===== === === === === ===== ===== =====')
print('            STRUK RINCIAN GAJI KARYAWAN            ')
print('---------------------------------------------------')
print('Nama Karyawan            : ' + namaKaryawan + '(Kode Karyawan : ' + kodeKaryawan + ')')
print('Golongan                 : ' + golKaryawan)
print('---------------------------------------------------')

if golKaryawan == 'A':
    gajiPokok = 10000000
    pot = 2.5
elif golKaryawan == 'B':
    gajiPokok = 8500000
    pot = 2.0
elif golKaryawan == 'C':
    gajiPokok = 7000000
    pot = 1.5
elif golKaryawan == 'D':
    gajiPokok = 5500000
    pot = 1.0
else:
    print('Maaf, golongan yang anda input tidak valid')

potongan = gajiPokok*pot/100
gajiBersih = gajiPokok-potongan

print('Gaji Pokok               : Rp. ' + str(gajiPokok))
print('Potongan ('+str(pot)+'%)          : Rp. ' + str(potongan))
print('---------------------------------------------------')
print('Gaji Bersih              : Rp. ' + str(gajiBersih))
