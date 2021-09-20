# Script Menghitung score BMI

def BMI(B, T):
    score = (B/((T/100)**2))
    if(score<18):
        status = 'KURUS'
    elif(score>=18) and (score<23):
        status = 'IDEAL'
    elif(score>=23) and (score<27):
        status = 'GEMUK'
    elif(score>=27) and (score<35):
        status = 'OBESITAS'
    elif(score>=35):
        status = 'OBESITAS MORBID'
    print('Status Berat Badan : ' + status)

Berat = int(input('Berat Badan (KG)   : '))
Tinggi = int(input('Tinggi Badan (CM)  : '))
BMI(Berat, Tinggi)
