# Script data sayur


sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print('Menu : ')
print('a. Tambah data sayur')
print('b. Hapus data sayur')
print('c. Tampilkan data sayur')

print('---------------------------------------------------')

while True:
    try:
        inputData = input('Pilihan anda (a/b/c) : ')
        
        if inputData == 'a':
            tambahSayur = str(input('Tambah data sayur    : '))
            sayur.append(tambahSayur)
        elif inputData == 'b':
            hapusSayur = str(input('Hapus data sayur     : '))
            sayur.remove(hapusSayur)
        elif inputData == 'c':
            print('Data sayur           :',sayur)
        else:
            print('Data yang anda input tidak valid')
        
    except ValueError:
        print('Data yang anda input tidak valid')
        break
