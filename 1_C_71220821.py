def reverse (isian) :
    hasil=""
    for i in isian:
        hasil=i+hasil
    return hasil
isian = input ("Masukan Kata atau angka :")
print(reverse(isian))
