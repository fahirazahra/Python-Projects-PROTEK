# Script kode program membuat formasi bintang dengan perintah center()
# Modifikasi script kode program pada Latihan no. 2

def bintang(n):

    bintang = int((n/2)+1)

    for x in range(n+1):
        print(('*'*(2*(x-1)+1)).center(10))

        if x == bintang:
            for x in range((int(n/2)+1)-1, 0, -1):
                print(('*'*(2*(x-1)+1)).center(10))
            break

# Jika n = 7
bintang(7)
print()