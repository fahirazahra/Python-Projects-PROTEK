# Script menghitung jarak tempuh pada mobil

def jarakTempuh(v, t):
    rumus = ((v*t)+1/2*(a*(t**2)))
    return rumus

v = int(input('Masukkan Kecepatan Mula-Mula (V0) : '))
a = int(input('Percepatan (a) : '))

t = 0
while (t<10):
    t+=1
    rumus = ((v*t)+1/2*(a*(t**2)))
    print('t = ', t, '', '', 'S(t) = ' + str(rumus))
t += 1
    
