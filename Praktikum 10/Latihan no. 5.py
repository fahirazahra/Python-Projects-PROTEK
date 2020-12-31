# Script kode program menjumlahkan dua bilangan yang terdapat pada file Latihan no. 5 (Data).txt

openFile = open('d:/Latihan no. 5 (Data).txt', 'r')
appendFile = open('d:/Latihan no. 5 (Hasil).txt', 'a')
readFile = openFile.readlines()

for x in range(len(readFile)):
    bilangan = readFile[x]
    A,B = bilangan.split('|')
    C = int(A) + int(B)
    D = str(C)
    appendFile.write(D + '\n')
appendFile.close()

result = open('d:/Latihan no. 5 (Hasil).txt')
print(result.read())

openFile.close()
result.close()