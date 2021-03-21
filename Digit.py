print('hasil digitAwal') #HIASAN
def digitAwal(a,b): #MENGAMBIL DUA ARGUMEN
    c = a**b #MENCARI PANGKAT
    d = str(c) #MENGUBAH MENJADI STRING AGAR DAPAT DIAMBIL AWALNYA
    for item in d: #PENJABARAN STRINGNYA
        return item #LANGSUNG AMBIL AWALNYA
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))

print('hasil digitAkhir') #HIASAN
def digitAkhir(a,b): #MENGAMBIL DUA ARGUMEN
    c = a**b #MENCARI PANGKAT
    d = str(c) #MENGUBAH MENJADI STRING AGAR DAPAT DIAMBIL AKHIRNYA
    for item in d: #PENJABARAN STRINGNYA
        item
    return item[-1:] #MENGAMBIL AWALNYA MENGGUNAKAN -1
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))