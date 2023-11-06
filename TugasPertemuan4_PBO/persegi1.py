# set nilai panjang dan lebar
panjang = 25
lebar = 4

# rumus
def HitungLuas(pj, lb):
    L = pj * lb
    return L

def HitungKeliling(pj, lb):
    K = (2 * pj)+(2 * lb)
    return K

# Gunakan fungsi untuk menghitung
Luas = HitungLuas(panjang, lebar)
Kel = HitungKeliling(panjang, lebar)

# Tampilkan Hasil
print("Panjang:", panjang)
print("Lebar:", lebar)
print("Luas:", Luas)
print("Keliling:", Kel)