data = {"genap": [], "ganjil": []}
while True:
    angka = int(input("Masukan angka [negatif untuk berhenti]: "))

    if angka < 0:
        break
    else:
        if angka % 2 == 0:
            data ["genap"].append(angka)
        else:
            data["ganjil"].append(angka)
    


    print(data)

def deret_ajaib_rekursif(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        return deret_ajaib_rekursif(n - 2) * ((n + 1) // 2)
def deret_ajaib_iteratif(n):
    deret = [1, 3, 5]  # Inisialisasi deret dengan suku 1, 3, dan 5
    for i in range(3, n):
        suku = deret[i - 2] * ((i + 1) // 2)  # Hitung suku ke-n
        deret.append(suku)
    return deret[n - 1]

import time

n_values = list(range(1, 51))
iterative_times = []
recursive_times = []

for n in n_values:
    start_time = time.time()
    deret_ajaib_iteratif(n)
    end_time = time.time()
    iterative_times.append(end_time - start_time)

    start_time = time.time()
    deret_ajaib_rekursif(n)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

# Membuat tabel catatan waktu
print("n\tIteratif (s)\tRekursif (s)")
for i in range(len(n_values)):
    print(f"{n_values[i]}\t{iterative_times[i]:.6f}\t{recursive_times[i]:.6f}")
    
