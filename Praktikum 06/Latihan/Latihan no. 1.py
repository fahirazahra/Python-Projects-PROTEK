def isPythagoras(a, b, c):
    if((a**2) == (c**2) - (b**2) or (b**2) == (c**2) - (a**2) or (c**2) == (a**2) + (b**2)):
        print(True)
    else:
        print(False)

# Soal A
isPythagoras(3, 4, 5)

# Soal B
isPythagoras(5, 9, 12)

# Soal C
isPythagoras(8, 6, 10)

# Soal D
isPythagoras(7, 8, 11)
