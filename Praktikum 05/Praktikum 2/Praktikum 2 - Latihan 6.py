# Modifikasi script game tebak angka

from random import randint
tebak = randint(0, 100)

print('Halo... nama saya Ms. Compy, saya sudah memilih bilangan bulat dari 0 hingga 100 secara acak. Yuk kita bermain tebak-tebakan!')

tebakanSalah = 0

while tebak:
    
    bil = int(input('Tebak Angka : '))
    tebakanSalah += 2
    score = 100-tebakanSalah

    if(bil<tebak):
         print('Hahaha.. tebakan anda terlalu kecil, coba lagi!')
    elif(bil>tebak):
        print('Waduh... besar sekali tebakannya. Ayo tebak lagi')
    else:
        print('YA! Tebakan anda BENAR. Selamat, kamu menang!')
        break

print('Score : ' + str(score))
