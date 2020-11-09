def luasSegitiga(alas, tinggi):
    luas = alas*tinggi/2
    return luas

alas = 10
tinggi = 20
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(alas, tinggi))

# Modifikasi soal Praktikum 2 - Langkah Kerja 1

def luasSegitiga2(alas, tinggi):
    luas2 = alas*tinggi/2
    return luas2

alas = 15
tinggi = 45
print('Luas segitiga 2 dg alas', alas,
      'dan tinggi', tinggi,
      'adalah', luasSegitiga2(alas, tinggi))

# Luas Total (Praktikum 2 - Langkah Kerja 8)

def luasTotalSegitiga(luas, luas2):
    luasTotal = luas + luas2
    return luasTotal

luas = 100
luas2 = 337.5
print('Luas total kedua segitiga diatas adalah', luasTotalSegitiga(luas, luas2))
