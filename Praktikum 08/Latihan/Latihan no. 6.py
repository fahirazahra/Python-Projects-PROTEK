# Script mengurutkan karakter huruf dalam data dari terbanyak-tersedikit

Data_Buah = ['apel', 'rambutan', 'jeruk']

def sortStringByChair(Data_Buah):
    Data_Buah.sort(reverse = True)
    return Data_Buah

sortedData = sortStringByChair(Data_Buah)

print('Diberikan sebuah list Data_Buah =',str(Data_Buah),'.',
      '\nJika dipanggil function sortStringByChar(Data_Buah), maka akan dihasilkan data list yang baru dengan susunan Data_Buah =',str(sortedData))
