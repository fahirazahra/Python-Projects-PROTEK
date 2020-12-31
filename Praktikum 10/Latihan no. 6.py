# Script kode program enkripsi string dengan sandi caesar

inputFile = input('Masukkan nama file : ')
banyaknya = int(input('Masukkan nilai n : '))
openFile = open(inputFile, 'r')
readFile = openFile.read()
karakter = list(readFile)
data = []

for x in karakter :
    Ascii_1 = ord(x)
    if Ascii_1 == 32:
        Ascii_2 = Ascii_1
    else:
        Ascii_2 = Ascii_1 + n

        if (Ascii_2 > 122):
            kurang = Ascii_2 - 26
        elif (Ascii_2 > 90 and Ascii_2 < 97) :
            Ascii_2 =Ascii_2 - 26
            
    character = chr(Ascii_2)
    data = data + [character]
    if not karakter :
        break
gabung = ''.join(isi)

result = open('d:/Latihan no. 6 (Teks Hasil).txt', 'a')
result.write(gabung)
result.close()