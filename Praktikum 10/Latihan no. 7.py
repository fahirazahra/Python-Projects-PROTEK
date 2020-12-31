# Script kode program mengembalikan Teks Hasil ke Teks Asli

openFile = open('d:\Latihan no. 6 (Teks Hasil)', 'r')
banyaknya = int(input('Banyaknya (n) : '))
readFile = openFile.read()
listData = list(readFile)
data = []

for x in listData:
    if (x == ' ') :
        y = ord(x)
    else :
        i = ord(x)
        y = i - n
        if (y < 65) :
            y = y + 26
        elif (90 < y and y < 97) :
            y = y + 26
    character = chr(y)
    data.append(character)
gabung = ','.join(data)

result = open('Latihan no. 7.txt', 'w')
result.write(gabung)
result.close()