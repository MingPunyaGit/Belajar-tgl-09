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