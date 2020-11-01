# Modifikasi script menghitung gaji karyawan

kodeKaryawan = input('Masukkan kode karyawan                          : ')
namaKaryawan = input('Masukkan nama karyawan                          : ')
golKaryawan = input('Masukkan golongan                               : ')
statusMenikah = input('Masukkan  status (1: Menikah, 2: Belum Menikah) : ')

if (statusMenikah == '1'):
    jumlahAnak = int(input('Masukkan jumlah anak                            : '))
    tunjangan  = 10/100
    status = 'Menikah'
elif (statusMenikah == '2'):
    jumlahAnak = 0
    tunjangan = 0
    status = 'Belum Menikah'
    
print('===== ===== ===== === === === === ===== ===== =====')
print('            STRUK RINCIAN GAJI KARYAWAN            ')
print('---------------------------------------------------')
print('Nama Karyawan              : ' + namaKaryawan + '(Kode Karyawan: ' + kodeKaryawan+')')
print('Golongan                   : ' + golKaryawan)
print('Status Menikah             : ' + status)
print('Jumlah Anak                : ' + str(jumlahAnak))
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

tunjanganAnak = (5/100)*jumlahAnak
totalTunjangan = gajiPokok*tunjangan
totalTunjanganAnak = gajiPokok*tunjanganAnak
potongan = gajiPokok*pot/100
gajiKotor = gajiPokok+totalTunjangan+totalTunjanganAnak
gajiBersih = gajiKotor-potongan

print('Gaji Pokok                 : Rp. ' + str(gajiPokok))
print('Tunjangan Istri/Suami (10%): Rp. ' + str(totalTunjangan))
print('Tunjangan Anak (5%/anak)   : Rp. ' + str(totalTunjanganAnak))
print('----------------------------------------------------')
print('Potongan ('+str(pot)+'%)            : Rp. ' + str(potongan))
print('Gaji Kotor                 : Rp. ' + str(gajiKotor))
print('---------------------------------------------------')
print('Gaji Bersih                : Rp. ' + str(gajiBersih))
