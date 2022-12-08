angka=input("Masukkan angka :")
hitung=input("Masukkan angka yg dihitung :")
hasil=0
for i in range(len(angka)) :
    if angka[i]==hitung:
        hasil += 1
print("Angka", hitung, "muncul sebanyak", hasil, "kali")
