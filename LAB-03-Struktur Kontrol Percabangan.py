#Nama   : Budi Gilbert Stephan Simbolon
#Universitas Kristen Duta Wacana

''' Buatlah algoritma yang menerima input koordinat (x,y) dalam sistem koordinat kartesius. 
Berdasarkan input koordinat tersebut, program akan menampilkan letak dari titik tersebut.

Ada 7 Kemungkinan :
1. Kuadran I (x-nya positif dan y-nya positif)
2. Kuadran II (x-nya negatif dan y-nya positif)
3. Kuadran III (x-nya negatif dan y-nya negatif)
4. Kuadran IV (x-nya positif dan y-nya negatif)
5. Di titik pusat (0,0) 
6. Menempel di sumbu X (y = 0) 
7. Menempel di sumbu Y (x = 0)

'''

''' 
Input :
x = ....
y = ....

Proses :
Mengelompokkan x dan y 

Output :
Letak dari titik (x,y)

'''

#input
x = int(input("Masukkan x = "))
y = int(input("Masukkan y = "))

#proses
titik_koordinat = str("(" + str(x) + "," + str(y) + ")")
if x > 0 and y > 0 :
    print("Titik " + titik_koordinat + " berada di kuadran I")
elif x < 0 and y > 0 :
    print("Titik " + titik_koordinat + " berada di kuadran II")
elif x < 0 and y < 0 :
    print("Titik " + titik_koordinat + " berada di kuadran III")
elif x > 0 and y < 0 :
    print("Titik " + titik_koordinat + " berada di kuadran IV")
elif x == 0 and y == 0 :
    print("Titik " + titik_koordinat + " berada di titik pusat")
elif x != 0 and y == 0 :
    print("Titik " + titik_koordinat + " menempel pada sumbu-X")
elif x == 0 and y != 0 :
    print("Titik " + titik_koordinat + " menempel pada sumbu-Y")
