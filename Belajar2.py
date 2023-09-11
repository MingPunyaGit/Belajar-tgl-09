data_buah = [
    {"nama" : "apel", "harga" : 10000},
    {"nama" : "jeruk", "harga" : 20000}, 
    {"nama" : "durian", "harga" : 120000}, 
    {"nama" : "kiwi", "harga" : 60000}, 
    {"nama" : "melon", "harga" : 27000}, 
    ]

for buah in data_buah:
    print(f'{buah["nama"]} - {buah["harga"]}')

harga_termahal = 0
buah_ternahal = ""
for buah in data_buah:
    if buah['harga'] > harga_termahal:
        harga_termahal = buah['harga']
        buah_ternahal = buah['harga']
    print(f'Nama Buah Termahal adalah {buah_ternahal} Dengan Harga {harga_termahal}')

batas = 100000
for index in range(len(data_buah)):
    if data_buah[index] ["harga"] < batas:
        del data_buah[index] 

print("Setelah semua buah di bawah batas harga di hapus")
for buah in data_buah:
    print(f'{buah["nama"]} - {buah["harga"]}')

def bagikan_kartu(jumlah_pemain):
    dek_kartu = list(range(1, 53))
    pemain_kartu = [[] for _ in range(jumlah_pemain)]

    for i, kartu in enumerate(dek_kartu):
        pemain_index = i % jumlah_pemain
        pemain_kartu[pemain_index].append(kartu)

    for i, kartu_pemain in enumerate(pemain_kartu):
        print(f'Pemain {i + 1}: {kartu_pemain}')

jumlah_pemain = int(input('Masukkan jumlah pemain: '))
bagikan_kartu(jumlah_pemain)
