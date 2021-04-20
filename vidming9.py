#Nama : Budi Gilbert Stephan Simbolon
#Universitas Kristen Duta Wacana

''' Buat program yang membaca bilangan bulat dari pengguna.
Setelah semua bilangan bulat telah dibaca, program Anda akan menampilkan semua 
angka negatif, angka nol, dan semua angka positif dalam grup list yang berbeda.
Dalam setiap grup, nomor harus ditampilkan berurutan dari terkecil hingga terbesar'''

'''
input:
- Menginputkan bilangan bulat
proses:
- Membuat List awal
- Menginputkan bilangan bulat
- Memisahkan negatif, nol, dan positifnya
- Masukkan setiap nilainya ke list
- Mengurutkan dari yang terkecil hingga ke terbesar
output:
3 grup list negatif, nol, dan positif
'''

negatif = []
nol = []
positif = []

inputan = input("Masukkan bilangan bulat (Kosongkan untuk selesai input) : ")
while inputan != "":
    angka = int(inputan)
    if angka < 0 and angka not in negatif:
        negatif.append(angka)
    elif angka > 0 and angka not in positif:
        positif.append(angka)
    elif angka == 0 and angka not in nol:
        nol.append(angka)
    inputan = input("Masukkan bilangan bulat (Kosongkan untuk selesai input) : ")
print("hasil pemisahan : ")
a = sorted(negatif)
b = sorted(nol)
c = sorted(positif)

print(a)
print(b)
print(c)
    
    
