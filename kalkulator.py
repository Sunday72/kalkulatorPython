print("Nama: Putra Setyonugroho")
print("Kelas: X RPL 1")
print("No. Absen: 19")

print("==========================")
a = int(input("masukkan angka a = "))
operator = input("masukkan operator aritmatika = ")
b = int(input("masukkan angka b = "))
if operator == '+':
    hasil = a + b
    print(a," + ",b," = ",hasil)
elif operator == '-':
    hasil = a - b
    print(a," - ",b," = ",hasil)
elif operator == '*':
    hasil = a * b
    print(a," * ",b," = ",hasil)
elif operator == '/':
    hasil = a / b
    print(a," / ",b," = ",hasil)
elif operator == '//':
    hasil = a // b
    print(a," // ",b," = ",hasil)
elif operator == '%':
    hasil = a % b
    print(a," % ",b," = ",hasil)
elif operator == '**':
    hasil = a ** b
    print(a," ** ",b," = ",hasil)
else:
    print("ANDA MEMASUKKAN ANGKA ATAU OPERATOR YANG SALAH!")
