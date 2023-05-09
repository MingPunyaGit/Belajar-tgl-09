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