# Script kode program menghitung selisih hari dari tanggal yang di input dengan hari ini

from datetime import *

def diffDate(x):
    formatDate = x.split('-')
    listDay = []

    for y in formatDate:
        listDay.append(int(y))

    day = date(listDay[0], listDay[1], listDay[2])
    today = datetime.date(datetime.now())

    difference = (day - today)
    result = abs(difference.days)

    return result

print('HARI INI ADALAH TANGGAL 12 JANUARI 2021')
print()
print('Selisih hari dibawah ini dari tanggal sekarang adalah ')
print()
print('14 Desember 2020 = ' + str(diffDate('2020-12-14')) + ' Hari ')
print('22 Juni 2021     = ' + str(diffDate('2021-06-22')) + ' Hari ')

print('-'*100)

print('Input tanggal lainnya dibawah ini jika ingin mengetahui selisih hari dari tanggal sekarang.')
print()

try:
    Tanggal = input('Masukkan Tanggal (YYYY-MM-DD)              : ')
    print()
    Selisih = diffDate(Tanggal)
    print('Selisih                                    : ' + str(Selisih) + ' Hari ')
except ValueError:
    print('INVALID INPUT')