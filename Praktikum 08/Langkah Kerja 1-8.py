a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a =', a)
print('b =', b)

print('--------------------------------------------------------------------------------------')
   
# Sisipkan nilai 10 ke dalam indeks ke-3 dari a
a.insert(3, 10)
print('Nilai 10 masuk ke dalam indeks ke-3 dari a    :', a)

# Sisipkan nilai 15 ke dalam indeks ke-2 dari b
b.insert(2, 15)
print('Nilai 15 masuk ke dalam indeks ke-2 dari b    :', b)

# Sisipkan nilai 4 ke indeks terakhir dari a
a = a+[4]
print('Nilai 4 masuk ke dalam indeks terakhir dari a :', a)

# Sisipkan nilai 8 ke indeks terakhir dari b
b = b+[8]
print('Nilai 8 masuk ke dalam indeks terakhir dari b :', b)

# Sorting secara ascending pada list a
a.sort()
print('Ascending sorting a                           :', a)

# Sorting secara ascending pada list b
b.sort()
print('Ascending sorting b                           :', b)

# Membuat list c yang elemennya merupakan sublist dari a (0 s/d 7)
c = a[0:7]
print('c                                             =', c)

# Membuat list d yang elemennya merupakan sublist dari b (2 s/d 9)
d = b[2:9]
print('d                                             =', d)

# Membuat list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya
e = []
for i in range(len(c)):
    jumlah = (c[i]+d[i])
    e = e+[jumlah]
print('e                                             =', e)

# Mengubah list e ke dalam tuple
Tuple = tuple(e)
print('Tuple e                                       =', Tuple)

# Mencari nilai minimal, maksimal, dan penjumlahan seluruh elemen dari e

# Maks
print('Nilai Maks dari e                             :', max(Tuple))

# Min
print('Nilai Min dari e                              :', min(Tuple))

# Jumlahan
print('Penjumlahan dari elemen e                     :', sum(Tuple))
