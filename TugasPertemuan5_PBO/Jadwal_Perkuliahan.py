import tkinter as tk
from tkinter import messagebox

def simpan_jadwal():
    nama_file = "jadwal_kuliah.txt"
    try:
        with open(nama_file, "a") as file:
            data_jadwal = f"{entry_hari.get()} - {entry_mata_kuliah.get()} - {entry_waktu.get()}\n"
            file.write(data_jadwal)
        messagebox.showinfo("Sukses", "Jadwal berhasil disimpan!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def tampilkan_jadwal():
    nama_file = "jadwal_kuliah.txt"
    try:
        with open(nama_file, "r") as file:
            isi_jadwal = file.read()
        messagebox.showinfo("Jadwal Kuliah", isi_jadwal)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Tidak ada jadwal kuliah yang tersimpan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat GUI
app = tk.Tk()
app.title("Aplikasi Jadwal Perkuliahan")
app.configure(bg="#e6e6e6")  # Set the background color of the main window

# Label dan Entry untuk Hari
label_hari = tk.Label(app, text="Hari:", bg="#e6e6e6")  # Set background color
label_hari.grid(row=0, column=0, padx=10, pady=10)
entry_hari = tk.Entry(app)
entry_hari.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk Mata Kuliah
label_mata_kuliah = tk.Label(app, text="Mata Kuliah:", bg="#e6e6e6")  # Set background color
label_mata_kuliah.grid(row=1, column=0, padx=10, pady=10)
entry_mata_kuliah = tk.Entry(app)
entry_mata_kuliah.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk Waktu
label_waktu = tk.Label(app, text="Waktu:", bg="#e6e6e6")  # Set background color
label_waktu.grid(row=2, column=0, padx=10, pady=10)
entry_waktu = tk.Entry(app)
entry_waktu.grid(row=2, column=1, padx=10, pady=10)

# Tombol Simpan Jadwal
button_simpan = tk.Button(app, text="Simpan Jadwal", command=simpan_jadwal, bg="#4CAF50", fg="white")  # Set background and text color
button_simpan.grid(row=3, column=0, columnspan=2, pady=10)

# Tombol Tampilkan Jadwal
button_tampilkan = tk.Button(app, text="Tampilkan Jadwal", command=tampilkan_jadwal, bg="#008CBA", fg="white")  # Set background and text color
button_tampilkan.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
app.mainloop()
