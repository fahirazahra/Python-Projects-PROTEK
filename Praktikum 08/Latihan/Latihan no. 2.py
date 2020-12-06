# Script menyusun inputan elemen data bilangan bulat dengan function dataStat


inputElemen = int(input('Berapa banyak elemen data yang anda inginkan? '))
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

def dataStat(x):
    Tuple = tuple(x)
    print('Data           = ', Tuple)
    
    a = ((sum(x))/len(x))
    b = max(Tuple)
    c = min (Tuple)
    data = [a, b, c]
    return data

hasil = dataStat(elemen)
print('---------------------------------------------------')
print('Hasil          = ', hasil)
