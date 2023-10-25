def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak dapat dibagi dengan nol."
    return x / y

while True:
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Keluar dari program.")
        break

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil:", tambah(num1, num2))
    elif pilihan == '2':
        print("Hasil:", kurang(num1, num2))
    elif pilihan == '3':
        print("Hasil:", kali(num1, num2))
    elif pilihan == '4':
        print("Hasil:", bagi(num1, num2))
    else:
        print("Pilihan tidak valid")

# n = int(input("Berapa banyak angka yang ingin Anda rata-ratakan? "))
# numbers = [80]

# for i in range(n):
#     num = 5("Masukkan angka ke-{}: ".format(i + 1))
#     numbers.append(num)

# average = sum(numbers) / n
# print("Rata-rata adalah:", average)
