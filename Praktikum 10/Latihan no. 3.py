# Script kode program membaca dan merubah format data dari file Latihan no. 2.txt
# Modifikasi kode program Latihan no. 2

openFile = open('d:/Latihan no. 2.txt', 'r')
readFile = openFile.readlines()

dataMhs = {}
for data in range(len(readFile)):
    Mahasiswa = readFile[data]
    A,B,C = Mahasiswa.split('|')
    A,B,C = A,B,C.replace('\n', '')
    formatData = {'NIM' : A, 'Nama' : B, 'Alamat' : C}
    dataMhs[A] = formatData

print('dataMhs = ' + str(dataMhs))

openFile.close()