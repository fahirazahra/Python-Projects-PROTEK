# Script hitung biaya penyewaan mobil
# dengan catatan 12 jam = 200.000, diatas 12 jam menjadi 10.000/jam
# Penyewaan di mulai dari pukul 06.00-23.50 (dalam hari yang sama)


tarifPertama = 200000
tarifKedua = 10000
jamKedua = 5
menitKedua = 50
tarifMenitKedua = ((tarifKedua/60)*50)
Biaya = tarifPertama+(tarifKedua*5)+tarifMenitKedua
print(Biaya)
