print("Nama: Putra Setyonugroho")
print("kelas: X RPL 1")
print("No. Absen: 19")
print("==========================")

bangunRuang = input('''
    1. kubus
    2. balok
    3. kerucut

    pilihlah salah satu bangun ruang diatas untuk dioperasikan!
    (gunakan huruf kecil semua) =  ''')

if bangunRuang == 'kubus':
    sisi = int(input("masukkan nilai sisi:"))
    volumeKubus = sisi**3
    luasPermukaanKubus = 6 * (sisi**2)
    print("Volumenya adalah", volumeKubus)
    print("luas permukaannya adalah", luasPermukaanKubus)
elif bangunRuang == 'balok':
    p = int(input("masukkan nilai panjang:"))
    l = int(input("masukkan nilai lebar:"))
    t = int(input("masukkan nilai tinggi:"))
    volumeBalok = p * l * t
    luasPermukaanBalok = 2 * ((p*l)+(p*t)+(l*t))
    print("Volumenya adalah", volumeBalok)
    print("luas permukaanya adalah", luasPermukaanBalok)
elif bangunRuang == 'kerucut':
    kerucut = input('''
    ingin menghitung volume atau luas permukaan?
    jawab = ''')
    if kerucut == 'volume':
        jariJari = int(input("masukkan nilai jari-jari:"))
        tinggi = int(input("masukkan nilai tinggi:"))
        volumeKerucut = (3.14 * (jariJari**2)*tinggi)/3
        print("volumenya adalah", volumeKerucut)
    elif kerucut == 'luas permukaan':
        jariJari = int(input("masukkan nilai jari-jari:"))
        pelukis = int(input("masukkan nilai garis pelukis:"))
        luasPermukaanKerucut = 3.14 * jariJari * (jariJari + pelukis)
        print("luas Permukaannya adalah", luasPermukaanKerucut)





