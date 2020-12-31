# Script kode program menentukan banyaknya bilangan genap dan ganjil pada data yang terdapat di file Latihan no. 1.txt

openFile = open('d:/Latihan no. 1.txt', 'r')
readFile = openFile.readlines()
genap = []
ganjil = []

for bilangan in range(len(readFile)):

    if '\n' in readFile[bilangan] == True:
        
        readFile[bilangan].replace('\n', '')

        if int(readFile[bilangan]) %2 == 0:
            genap.append(readFile[bilangan])
        elif int(readFile[bilangan]) %2 == 1:
            ganjil.append(readFile[bilangan])
    
    else:
        if int(readFile[bilangan]) %2 == 0:
            genap.append(readFile[bilangan])
        elif int(readFile[bilangan]) %2 == 1:
            ganjil.append(readFile[bilangan])

print('Banyaknya bilangan genap  : {0}'.format(len(genap)))
print('Banyaknya bilangan ganjil : {0}'.format(len(ganjil)))