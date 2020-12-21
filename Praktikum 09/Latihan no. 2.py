# Script kode program membuat formasi bintang dengan perintah center()

def bintang(n):

    for x in range(n+1):
        print(('*'*(2*(x-1)+1)).center(10))

# Jika n = 4
bintang(4)
print()