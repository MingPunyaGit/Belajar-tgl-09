# indoing = dict()
# # print(dir(indoing))
# # donder method
# indoing['makan'] = 'eat'
# indoing['lari'] = 'run'
# indoing['minum'] = 'drink'
# indoing['belajar'] = 'study'
# # print(indoing['makan'])
# # print(len(indoing))
# # print(indoing.keys())
# # print(indoing.values())
# indoing['lompat'] = 'jump'
# # print(len(indoing))
# del indoing['belajar']
# print(indoing)
# khs = {
#     '71222098' : ['Tekkom', 'jarkom', 'logmat'],
#     '71222357' : ['PAK', 'Tekkom', 'logmat'],
# }
# # for key in khs.keys():
#     # print(f"NIM: {key}, matkul: {khs[key]}")

# del khs['71222098'][0]
# print(khs['71222098'])

# khs['71222098'].append("IMK")
# print(khs)

# def pangkati(n, pangkat):
#     kamus = dict()
#     for x in range(1,n+1):
#         kamus[x]=x**pangkat
#     print("Dictionary = ", kamus)


# n= int(input("Input data = "))
# pangkat= int(input("Input pangkat = "))
# pangkati(n, pangkat)

# data = [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# print("Data asli: ",data)
# hasil = []
# for d in data:
#     for value in d.values():
#         if hasil.count(value) == 0:
#             hasil.append(value)
        
# print("Nilai Unik: ",hasil)

kartukeluarga = {
    'Kepala keluarga': 'Munjahit',
    'Alamat': 'Sokokulon',
    'RT/RW': '3/2',
    'Kelurahan/Desa': 'Soko Kulon',
    'Kecamatan': 'Margorejo',
    'Kabupaten/Kota': 'Pati',
    'Kode Pos': '56194',
    'Provinsi':'Jawa Tengah',
    'anggota' : 'Munjahit'
}

Lakukan perbandingan kinerja dari fungsi iteratif dan fungsi rekursif untuk mendapatkan suku ke-n dari suatu Deret Ajaib. Perbandingan dilakukan dengan mencatat waktu yang diperlukan untuk mendapatkan suku Ajaib ke-1 sampai ke-50(nilai n) dengan kedua fungsi tersebut. Kemudian berdasarkan catatan waktu tersebut, buatlah tabel catatan waktu terhadap n.

Anda harus menghasilkan:

Source code fungsi Deret Ajaib ke-n secara iteratif dan rekursif
Tabel catatan waktu dari kedua fungsi tersebut, dengan nilai n= 1 sampai 50
KETERANGAN: Deret ajaib ke-n maksudnya adalah suku ke-n dari deret bilangan yang 3 angka pertamanya sudah di tentukan yaitu 1,3,5 dan suku ke-4 dihitung dari suku ke-(n-2)*suku ke-(n/2) dengan pembulatan ke atas. U1 = 1 U2 = 3 U3 = 5 U4 = U(n-2) * bulatkan((n : 2))

Misal: suku ke-4 dihitung dari suku ke-(n/2) yaitu 3 dikali dengan suku ke-(n/2) yaitu 2, maka suku ke-4 adalah 32 = 6. Kemudian suku ke-5 dihitung dari n-2 yaitu 5 dikali dengan 5/2 yaitu 3. Maka suku ke-7 adalah 53 = 15

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
    new_data = {
        'NIM': input('Masukkan NIM mahasiswa: '),
        'nama': input('Masukkan nama mahasiswa: '),
        'jurusan': input('Masukkan jurusan mahasiswa: ')
    }
    
    jumlah_matkul = int(input('Masukkan jumlah mata kuliah: '))
    matkul_list = []

    for i in range(jumlah_matkul):
        matkul_list.append(input(f'Masukkan nama mata kuliah ke-{i + 1}: '))
    
    new_data['mata_kuliah'] = matkul_list
    data.append(new_data)

# Menyimpan data ke dalam file JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print('Data berhasil ditambahkan.')





