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
