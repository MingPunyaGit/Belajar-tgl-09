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
  
