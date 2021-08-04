print("Nama: Putra Setyonugroho")
print("Kelas: X RPL 1")
print("No. Absen: 19")

print("==========================")

############################################################
##### OPERASI PERHITUNGAN LUAS DAN VOLUME BANGUN DATAR #####
############################################################

bangunDatar = input('''
    1. persegi
    2. persegi panjang
    3. segitiga
    4. trapesium
    5. lingkaran

    pilihlah salah satu bangun datar diatas untuk dioperasikan!
    (gunakan huruf kecil semua) =  ''')

if bangunDatar == 'persegi':
    sisi = int(input("Masukkan sisi persegi: "))
    luasPersegi = sisi * sisi
    kelilingPersegi = sisi * 4
    print("luasnya adalah", luasPersegi)
    print("kelilingnya adalah", kelilingPersegi)
elif bangunDatar == 'persegi panjang':
    p = int(input("masukkan nilai panjang:"))
    l = int(input("masukkan nilai lebar:"))
    luasPersegiPanjang = p * l
    kelilingPersegiPanjang = 2 * (p + l)
    print("luasnya adalah", luasPersegiPanjang)
    print("kelilingnya adalah", kelilingPersegiPanjang)
elif bangunDatar == 'segitiga':
    segitiga = input('''
    ingin menghitung luas atau keliling?
    jawab = ''')
    if segitiga == 'luas':
        alas = int(input("masukkan nilai alas:"))
        tinggi = int(input("masukkan nilai tinggi:"))
        luasSegitiga = (alas * tinggi) / 2
        print("luasnya adalah", luasSegitiga)
    elif segitiga == 'keliling':
        sisi1 = int(input("masukkan sisi 1: "))
        sisi2 = int(input("masukkan sisi 2: "))
        sisi3 = int(input("masukkan sisi 3: "))
        kelilingSegitiga = sisi1 + sisi2 + sisi3
        print("kelilingnya adalah", kelilingSegitiga)
elif bangunDatar == 'trapesium':
    trapesium = input('''
        ingin menghitung luas atau keliling?
        jawab = ''')
    if trapesium == 'luas':
        a = int(input("masukkan alas bawah:"))
        b = int(input("masukkan alas atas:"))
        t = int(input("masukkan tinggi:"))
        luasTrapesium = ((a + b)*t)/2
        print("luasnya adalah", luasTrapesium)
    elif trapesium == 'keliling':
        sisi_a = int(input("masukkan sisi 1:"))
        sisi_b = int(input("masukkan sisi 2:"))
        sisi_c = int(input("masukkan sisi 3:"))
        sisi_d = int(input("masukkan sisi 4:"))
        kelilingTrapesium = sisi_a + sisi_b + sisi_c + sisi_d
        print("kelilingnya adalah", kelilingTrapesium)
elif bangunDatar == 'lingkaran':
    lingkaran = input('''
            ingin menghitung luas atau keliling?
            jawab = ''')
    if lingkaran == 'luas':
        diameter = int(input("masukkan nilai diameter:"))
        luasLingkaran = (3.14 * (diameter**2))/4
        print("luasnya adalah", luasLingkaran)
    elif lingkaran == 'keliling':
        jariJari = int(input("masukkan nilai jari-jari:"))
        kelilingLingkaran = 2*(3.14 * jariJari)
        print("kelilingnya adalah", kelilingLingkaran)



