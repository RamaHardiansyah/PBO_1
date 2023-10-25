berat_badan = 80
tinggi = 190
bmi = berat_badan / (tinggi * 2)
if bmi < 18.5:
    kategori = "Kurang berat badan"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal"
elif 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
else:
    kategori = "Obesitas"
print(f"BMI Anda adalah {bmi}m")
print("Kategori BMI Anda:",kategori)