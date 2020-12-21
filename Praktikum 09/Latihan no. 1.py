# Script kode program mengubah huruf 't' pada kata 'Matematika' dengan perintah replace()

def ubahHuruf (teks, a, b):

    return teks.replace(a, b)
    
huruf = 'Matematika'
print(ubahHuruf(huruf, 't', 's'))