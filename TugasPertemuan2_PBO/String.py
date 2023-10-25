# Menggabungkan beberapa string
nama_depan = "Rama"
nama_belakang = "Hardiansyah"
nama_lengkap = nama_depan + " " + nama_belakang

panjang_nama = len(nama_lengkap)

d = "d"
status = d in nama_lengkap

D = "D"
status = D in nama_lengkap

D = "D"
status = D not in nama_lengkap

print("Nama Lengkap:", nama_lengkap)
print("Panjang Nama:", panjang_nama)
print("string " + d + " ada di " + nama_lengkap + " = "+ str(status))
print(D + " ada di " + nama_lengkap + " = "+ str(status))
print(D + " tidak ada di " + nama_lengkap + " = "+ str(status))
print("index ke-1: " + nama_lengkap[1])
print("index ke-1: " + nama_lengkap[-1])
print("index ke-5: " + nama_lengkap[5])
print("index ke-5: " + nama_lengkap[-5])
print("index ke-[0:4]:" + nama_lengkap[0:4])
print("index ke-[5:16]:" + nama_lengkap[5:16])
print("paling besar : " + max(nama_lengkap))