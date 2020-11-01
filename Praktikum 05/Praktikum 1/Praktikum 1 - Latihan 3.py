# Modifikasi kedua script Status Kelulusan Mahasiswa

nilaiBI = int(input('Masukkan nilai Bahasa Indonesia : '))
nilaiIPA = int(input('Masukkan nilai IPA              : '))
nilaiMTK = int(input('Masukkan nilai Matematika       : '))



if((nilaiBI >= 0) and (nilaiBI <= 100)) and ((nilaiIPA >= 0) and (nilaiIPA <= 100)) and ((nilaiMTK >= 0) and (nilaiMTK <= 100)):
        if(nilaiBI >= 60) and (nilaiIPA >= 60) and (nilaiMTK >= 70):
                SK = 'LULUS'
        else:
                SK = 'TIDAK LULUS'

        print('Status Kelulusan                : ' + SK)
        print('Sebab : ')

        if(nilaiBI < 60):
                print('- Nilai Bahasa Indonesia kurang dari 60')
        if(nilaiIPA < 60):
                print('- Nilai IPA kurang dari 60')
        if(nilaiMTK < 70):
                print('- Nilai Matematika kurang dari 70')
else:
        print('Maaf, nilai yang anda input tidak valid.')


