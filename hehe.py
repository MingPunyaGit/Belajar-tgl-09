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








