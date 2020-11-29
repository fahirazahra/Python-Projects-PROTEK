# Modifikasi kode program langkah kerja 3

file = open('d:/data3.txt', 'r')
sum = 0
try:
    for data in file:
        try:
            sum = sum + int(data)
        except ValueError:
            print('Bukan bilangan bulat')
    print(sum)
except FileNotFoundError:
    print('File tidak ditemukan')
