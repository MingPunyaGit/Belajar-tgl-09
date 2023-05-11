import math
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