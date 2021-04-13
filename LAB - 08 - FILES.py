#Nama   : Budi Gilbert Stephan Simbolon
#Universitas Kristen Duta Wacana

""" Python menggunakan karakter # untuk menandai awal komentar. 
Anda diminta untuk membuat program yang menghapus semua komentar dari file sumber Python.
Periksa setiap baris dalam file untuk menentukan apakah ada karakter #. 
Jika ya, program Anda harus menghapus semua karakter dari karakter # hingga akhir baris """

"""
input:
- Menginputkan file yang akan dicek dan dieksekusi

proses:
- Menginputkan file yang akan dicek dan dieksekusi
- Mengecek setiap barisnya
- Menghapus baris yang memiliki komentar
- Buat file baru hasil pengecekkan dan pengeksekusian

output:
- file baru hasil pengecekkan dan pengeksekusian (file tidak mengandung komentar)

"""

try:
    nama_file = input("Masukkan nama file Python: ")
    buka_file = open(nama_file, "r")
except:
    print("Terjadi masalah pada saat membuka file")
    print("Keluar...")
    quit()

try:
    namaO_file = input("Masukkan nama file Python hasil pengeksekusian: ")
    bukaO_file = open(namaO_file, "w")
except:
    print("Terjadi masalah pada saat membuka file")
    print("Keluar...")
    quit()

try:
    for line in buka_file:
        posisi = line.find("#")
        if posisi > -1:
            line = line[0 : posisi]
            line = line + "\n"
        bukaO_file.write(line)
    buka_file.close()
    bukaO_file.close()
except:
    print("Terjadi masalah pada saat membuka file")
    print("Keluar...")
    

