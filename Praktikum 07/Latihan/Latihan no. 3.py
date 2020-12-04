# Script menghitung rata-rata

print('--------------------------------------------------------------')
print('                 PROGRAM HITUNG RATA-RATA')
print('--------------------------------------------------------------')


BilBul = int(input('Masukkan bilangan bulat : '))

while True:
    try:
        jumlah = 0
        bilangan = 0
        jumlah += BilBul
        bilangan += 1
        ulang = str(input('Lagi (yes/no)? '))
        if(ulang == 'no'):
            break
        else:
            continue
    except ValueError:
        print('Bilangan yang anda input bukan bilangan bulat.')
        continue

RataRata = (jumlah/bilangan)
print('Rata-ratanya adalah ', RataRata)
