'''Buatlah program yang akan menghitung setiap huruf vokal dari kata/kalimat yang inputkan'''

'''
Input :
1. Inputan kata/kalimat
2. Nilai awal

Proses :
1. program akan menghitung panjang kata/kalimat
2. while untuk menghitung setiap huruf vokal

Output :
jumlah dari setiap huruf vokal dari kata/kalimat yang diinputkan
'''

inputan = input("Masukkan kata/kalimat : ")

a = 0
i = 0
u = 0
e = 0
o = 0

Panjang_kata = len(inputan)

x = 0
while x < Panjang_kata:
    if(inputan[x]=="a" or inputan[x]=="A"):
        a += 1
    if(inputan[x]=="i" or inputan[x]=="I"):
        i += 1
    if(inputan[x]=="u" or inputan[x]=="U"):
        u += 1
    if(inputan[x]=="e" or inputan[x]=="E"):
        e += 1
    if(inputan[x]=="o" or inputan[x]=="O"):
        o += 1
    x += 1

print("Banyak huruf a = ", a)
print("Banyak huruf i = ", i)
print("Banyak huruf u = ", u)
print("Banyak huruf e = ", e)
print("Banyak huruf o = ", o)