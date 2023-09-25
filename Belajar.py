# data_mahasiswa = {
#     "nim" : "71220000",
#     "nama" : "tejo",
#     "prodi" : "informatika",
#     "ipk" : 2.3,
#     "smester" : 4,
#     "matkul" : [
#         {"nama" : "IMK", "sks" : 3, "nilai" : "B"},
#         {"nama" : "Jarkom", "sks" : 3, "nilai" : "C"},
#         {"nama" : "Alpro", "sks" : 5, "nilai" : "A"},
#     ],
# } 
# print(data_mahasiswa["nama"])
# print(f"IPK-nya : {data_mahasiswa['ipk']}")
# print(f'Sudah mengambil {len(data_mahasiswa["matkul"])}matkul')
# transkrip = data_mahasiswa["matkul"]
# for matkul in transkrip:
#     if matkul["nilai"] == "E" :
#         print(matkul["nama"])
#     total = total + matkul["sks"]
# print(f"Total sks yang sudah di ambil: {total} sks")


print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')

if operasi in ('1', '2', '3', '4'):
    bilangan_1 = float(input('Masukkan bilangan pertama: '))
    bilangan_2 = float(input('Masukkan bilangan kedua: '))

    if operasi == '1':
        hasil = bilangan_1 + bilangan_2
        print('Hasil: ', hasil)
    elif operasi == '2':
        hasil = bilangan_1 - bilangan_2
        print('Hasil: ', hasil)
    elif operasi == '3':
        hasil = bilangan_1 * bilangan_2
        print('Hasil: ', hasil)
    elif operasi == '4':
        if bilangan_2 != 0:
            hasil = bilangan_1 / bilangan_2
            print('Hasil: ', hasil)
        else:
            print('Tidak bisa membagi dengan 0')
else:
    print('Pilihan operasi tidak valid')


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
        print("=== INFORMASI MAHASISWA ===")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("IPS:", format(self.ips, ".2f"))

    def hitung_ips(self):
        total_nilai = 0
        total_sks = 0

        jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
        for i in range(jumlah_matkul):
            nama_matkul = input("Masukkan nama mata kuliah: ")
            nilai_matkul = input("Masukkan nilai mata kuliah (A, A-, B+, dst.): ")
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

            total_nilai += nilai_angka.get(nilai_matkul.upper(), 0) * sks
            total_sks += sks

        if total_sks > 0:
            self.ips = total_nilai / total_sks


# Contoh penggunaan kelas Mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM mahasiswa: ")
prodi = input("Masukkan prodi mahasiswa: ")

mahasiswa = Mahasiswa(nama, nim, prodi)
mahasiswa.hitung_ips()
mahasiswa.print_informasi()

  
