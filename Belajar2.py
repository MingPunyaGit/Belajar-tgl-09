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

def bagikan_kartu(jumlah_pemain):
    dek_kartu = list(range(1, 53))
    pemain_kartu = [[] for _ in range(jumlah_pemain)]

    pemain_index = 0  # Variabel penghitung pemain

    for kartu in dek_kartu:
        pemain_kartu[pemain_index].append(kartu)
        pemain_index = (pemain_index + 1) % jumlah_pemain

    for i, kartu_pemain in enumerate(pemain_kartu):
        print(f'Pemain {i + 1}: {kartu_pemain}')

jumlah_pemain = int(input('Masukkan jumlah pemain: '))
bagikan_kartu(jumlah_pemain)

def bagikan_kartu(jumlah_pemain):
    dek_kartu = list(range(1, 53))
    pemain_kartu = [[] for _ in range(jumlah_pemain)]

    pemain_index = 0
    kartu_index = 0

    while kartu_index < len(dek_kartu):
        kartu = dek_kartu[kartu_index]
        pemain_kartu[pemain_index].append(kartu)
        pemain_index = (pemain_index + 1) % jumlah_pemain
        kartu_index += 1

    for i, kartu_pemain in enumerate(pemain_kartu):
        print(f'Pemain {i + 1}: {kartu_pemain}')

jumlah_pemain = int(input('Masukkan jumlah pemain: '))
bagikan_kartu(jumlah_pemain)

def bagikan_kartu(jumlah_pemain):
    dek_kartu = list(range(1, 53))
    pemain_kartu = [[] for _ in range(jumlah_pemain)]

    pemain_index = 0  # Variabel penghitung pemain

    for kartu in dek_kartu:
        pemain_kartu[pemain_index].append(kartu)
        pemain_index = (pemain_index + 1) % jumlah_pemain

    for i, kartu_pemain in enumerate(pemain_kartu):
        print(f'Pemain {i + 1}: {kartu_pemain}')

jumlah_pemain = int(input('Masukkan jumlah pemain: '))
bagikan_kartu(jumlah_pemain)

class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.ips = 0

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_prodi(self):
        return self.prodi

    def get_ips(self):
        return self.ips

    def print_informasi(self):
        print("=== INFORMASI MAHASISWA ====")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("IPS:", self.ips)

    def hitung_ips(self):
        jumlah_nilai = 0
        jumlah_sks = 0

        # Membaca input pengguna
        jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

        for i in range(jumlah_mata_kuliah):
            nama_mata_kuliah = input("Masukkan nama mata kuliah: ")
            nilai_mata_kuliah = input("Masukkan nilai mata kuliah: ")
            sks_mata_kuliah = int(input("Masukkan SKS mata kuliah: "))

            # Konversi nilai huruf menjadi nilai angka
            nilai_angka = {
                "A": 4,
                "A-": 3.7,
                "B+": 3.3,
                "B": 3,
                "B-": 2.7,
                "C+": 2.3,
                "C": 2,
                "D": 1,
                "E": 0
            }

            # Menghitung total nilai
            jumlah_nilai += nilai_angka[nilai_mata_kuliah] * sks_mata_kuliah

            # Menghitung total SKS
            jumlah_sks += sks_mata_kuliah

        # Menghitung IPS
        self.ips = jumlah_nilai / jumlah_sks

# Deklarasi variable
nama = "Budi"
nim = 71210000
prodi = "FTI"

# Membuat object Mahasiswa
mahasiswa = Mahasiswa(nama, nim, prodi)

# Menghitung IPS
mahasiswa.hitung_ips()

# Menampilkan informasi mahasiswa
mahasiswa.print_informasi()

# Menampilkan output
print(mahasiswa.nama, mahasiswa.nim, mahasiswa.prodi, mahasiswa.ips)
            


