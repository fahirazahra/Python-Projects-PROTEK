# Script menghitung kuadrat inputan elemen data bilangan bulat

inputElemen = int(input('Masukkan elemen data bilangan bulat yang anda inginkan : '))
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

def kuadrat(bil):
    Tuple = tuple(bil)
    print('Data           = ', Tuple)

    print('-------------------------------------------------------------')

    for i in range(len(bil)):
        angka = ((bil[i])**2)
        elemen.append(angka)
    return elemen

hasil = kuadrat(elemen)
print('Data kuadrat   = ', hasil)

    
