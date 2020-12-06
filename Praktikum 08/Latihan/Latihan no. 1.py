# Script menyusun inputan elemen data bilangan bulat dari terbesar-terkecil

inputElemen = int(input('Masukkan banyaknya elemen data yang anda inginkan! '))
elemen = []
i = 1
                  
while True:
    try:
        inputAngka = int(input('Masukkan angka : '))
        elemen.append(inputAngka)
        if i == inputElemen:
            break
        i = i+1
    except ValueError:
        print('Data yang anda input tidak valid')

print('--------------------------------------------------------')

elemen.sort(reverse = True)
print('Data           = ', elemen)
