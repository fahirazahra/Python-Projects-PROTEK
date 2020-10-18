# Script hitung waktu mobil sampai ke kota C
# dengan jarak kota A ke B adalah 125 km dan kecepatan rata-rata 62km/jam
# jarak kota B ke C adalah 256 km dan kecepatan rata-rata 70km/jam
# berangkat dari kota A pukul 06.00 dan sempat istirahat di kota B selama 45 menit


jarak1 = 125
kecepatan1 = 62
jarak2 = 256
kecepatan2 = 70
menitIstirahat = 45
jamIstirahat = menitIstirahat/60
waktuSampai = ((jarak1/kecepatan1)+jamIstirahat+(jarak2/kecepatan2))
print(waktuSampai)
