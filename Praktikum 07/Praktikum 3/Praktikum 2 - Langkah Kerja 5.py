# membuka dan mau membaca file d:/data2.txt
try:
    file = open("d:/data2.txt", "r")
except FileNotFoundError:
    print('File tidak ditemukan')

# baca baris pertama dari file
# simpan ke dalam variabel bil1 sbg integer
try:
    bil1 = int(file.readline())

# baca baris kedua dari file
# simpan ke dalam variabel bil2 sbg integer
    bil2 = int(file.readline())

# hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')
