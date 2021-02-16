#Nama : Budi Gilbert Stephan Simbolon
#Universitas Kristen Duta Wacana

''' Suatu pekerjaan dapat diselesaikan oleh 42 pekerja dalam waktu 50 hari. 
Agar pekerjaan tersebut dapat selesai dalam waktu 35 hari, berapakah tambahan pekerja yang diperlukan?

P1/P2 = W2/W1

P1 = Jumlah pekerja (awal)
W1 = Jumlah waktu yang dibutuhkan (awal)
P2 = Jumlah pekerja (akhir)
W2 = Jumlah waktu yang dibutuhkan (akhir)
T = Tambahan pekerja yang diperlukan

'''

''' 
Input : P1 = 42 pekerja ; W1 = 50 hari ; W2 = 35 hari

Proses :
Mencari nilai dari P2
Mencari nilai T

Output: Jumlah tambahan pekerja yang dibutuhkan

'''

#inputan
P1 = 42
W1 = 50
W2 = 35

#Mencari nilai P2
P2 = P1*W1/W2
P2 = int(P2)

#Mencari nilai T
T = P2 - P1
T = int(T)

#Output
print("Jumlah tambahan pekerja yang dibutuhkan adalah "+ str(T) + " pekerja")