# Script kode program memasukkan list nilai ke dalam tabel

nilai = [{'NIM' : 'A01', 'Nama' : 'Agustina', 'MID' : 50,  'UAS' : 80},
         {'NIM' : 'A02', 'Nama' : 'Budi',     'MID' : 40,  'UAS' : 90},
         {'NIM' : 'A03', 'Nama' : 'Chicha',   'MID' : 100, 'UAS' : 50},
         {'NIM' : 'A04', 'Nama' : 'Donna',    'MID' : 20,  'UAS' : 100},
         {'NIM' : 'A05', 'Nama' : 'Fatimah',  'MID' : 70,  'UAS' : 100}]

print('='*70)
print(('NIM'.ljust(15, ' ')), ('Nama'.ljust(10, ' ')), ('Nilai MID'.rjust(20, ' ')), ('Nilai UAS'.rjust(20, ' ')))
print('-'*70)

for listNilai in nilai:

    print(str(listNilai['NIM']).ljust(15, ' '),
          str(listNilai['Nama']).ljust(10, ' '),
          str(listNilai['MID']).rjust(20, ' '),
          str(listNilai['UAS']).rjust(20, ' '))

print('-'*70)