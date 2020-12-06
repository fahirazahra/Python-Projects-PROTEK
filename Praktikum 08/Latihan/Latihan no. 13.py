# Script menentukan nilai Mahasiswa

MID = []
UAS = []
nilaiAkhir = []
nilaiTertinggi = []

namaMahasiswa = [{'NIM' : 'A01', 'Nama' : 'Amir', 'MID' : 50, 'UAS' : 80},
                 {'NIM' : 'A02', 'Nama' : 'Budi', 'MID' : 40, 'UAS' : 90},
                 {'NIM' : 'A03', 'Nama' : 'Cici', 'MID' : 50, 'UAS' : 50},
                 {'NIM' : 'A04', 'Nama' : 'Dedi', 'MID' : 20, 'UAS' : 30},
                 {'NIM' : 'A05', 'Nama' : 'Fifi', 'MID' : 70, 'UAS' : 40}]


def NilaiMax(namaMahasiswa):
    for i in namaMahasiswa:
        hasilAkhir = ((i['MID']+(2*i['UAS']))/3)
        nilaiAkhir.append(hasilAkhir)
        
    nilaiTertinggi = (nilaiAkhir.index(max(nilaiAkhir)))

    dataMahasiswa = {'NIM' : namaMahasiswa[nilaiTertinggi]['NIM'], 'Nama' : namaMahasiswa[nilaiTertinggi]['Nama']}
    return dataMahasiswa

Tertinggi = NilaiMax(namaMahasiswa)
print('Nilai akhir : ',str(Tertinggi['Nama']),',','NIM',Tertinggi['NIM'])
