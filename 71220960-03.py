ygimport math
def hitung_jarak(p1,p2):
    return math.sqrt((p2[0] - p1[0]) **2 + (p2[1] - p1[1])**2)

def hitung_keliling_segitiga(titik):
    A = titik["A"]
    B = titik["B"]
    C = titik["C"]

    sisi_AB = hitung_jarak(A, B)
    sisi_BC = hitung_jarak(B, C)   
    sisi_CA = hitung_jarak(C, A)

    keliling = sisi_AB + sisi_BC + sisi_CA
    return keliling

input_test = {"A":[1,1], "B": [5,1],"C":[3,7]}
keliling_segitiga = hitung_keliling_segitiga(input_test)

def hitung_keliling_segitiga(titik):
    J = titik["J"]
    K = titik["K"]
    L = titik["L"]

    sisi_JK = hitung_jarak(J, K)
    sisi_KL = hitung_jarak(K, L)
    sisi_LJ = hitung_jarak(L, J)

    keliling = sisi_JK + sisi_KL + sisi_LJ
    return keliling
    
input_test2 = {"J":[1,3], "K":[4,5], "L":[3,0]}
keliling_segitiga2 = hitung_keliling_segitiga(input_test2)



print("Keliling segitiga" ,keliling_segitiga)
print("Keliling segitiga" ,keliling_segitiga2)

import json

# Membaca data dari file JSON (jika sudah ada)
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    # Jika file tidak ditemukan, inisialisasi data sebagai list kosong
    data = []

# Memasukkan jumlah mahasiswa baru
jumlah_mahasiswa = int(input('Masukkan jumlah mahasiswa baru: '))

for _ in range(jumlah_mahasiswa):
    nim = input('Masukkan NIM mahasiswa: ')
    nama = input('Masukkan nama mahasiswa: ')
    jurusan = input('Masukkan jurusan mahasiswa: ')
    
    jumlah_matkul = int(input('Masukkan jumlah mata kuliah: '))
    matkul_list = []

    for i in range(jumlah_matkul):
        matkul = input(f'Masukkan nama mata kuliah ke-{i + 1}: ')
        matkul_list.append(matkul)
    
    new_data = {
        'NIM': nim,
        'nama': nama,
        'jurusan': jurusan,
        'mata_kuliah': matkul_list
    }
    
    data.append(new_data)
    
    print("=== Data berhasil ditambahkan ===")

# Menyimpan data ke dalam file JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print('Data berhasil ditambahkan.')


class Mahasiswa:

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.ips = 0

    def get_nama(self):
        return self.nama

    def set_nama(self, nama):
        self.nama = nama

    def get_nim(self):
        return self.nim

    def set_nim(self, nim):
        self.nim = nim

    def get_prodi(self):
        return self.prodi

    def set_prodi(self, prodi):
        self.prodi = prodi

    def get_ips(self):
        return self.ips

    def set_ips(self, ips):
        self.ips = ips

    def print_informasi(self):
        print("=== INFORMASI MAHASISWA ===")
        print("Nama: " + self.nama)
        print("NIM: " + self.nim)
        print("Prodi: " + self.prodi)

    def hitung_ips(self):
        total_nilai = 0
        total_sks = 0

        jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
        for i in range(jumlah_matkul):
            nama_matkul = input("Masukkan nama mata kuliah: ")
            nilai_matkul = input("Masukkan nilai mata kuliah: ")
            sks = int(input("Masukkan SKS mata kuliah: "))

            nilai_angka = {
                "A": 4,
                "A-": 3.7,
                "B+": 3.3,
                "B": 3,
                "B-": 2.7,
                "C+": 2.3,
                "C": 2,
                "D": 1,
                "E": 0,
            }

            total_nilai += nilai_angka[nilai_matkul] * sks
            total_sks += sks

        self.ips = round(total_nilai / total_sks, 2)


if __name__ == "__main__":
    mhs = Mahasiswa("Budi", "71210000", "FTI")

    mhs.print_informasi()

    mhs.hitung_ips()

    print("IPS:", mhs.get_ips())
    

