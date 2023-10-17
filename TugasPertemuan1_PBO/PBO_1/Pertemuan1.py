from tkinter import Tk, Frame, Label, Entry, Button, YES, BOTH, END, W
import math
from tkinter import ttk

class AplikasiLuasBangun:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Aplikasi Menghitung Keliling dan Luas Bangun Datar")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.tabControl = None
        self.aturanKomponen()
        self.parent.geometry("1000x500")


    def aturanKomponen(self):
        self.tabControl = ttk.Notebook(self.parent)
        

        self.tabPersegi = ttk.Frame(self.tabControl)
        self.tabPersegiPanjang = ttk.Frame(self.tabControl)
        self.tabBelahKetupat = ttk.Frame(self.tabControl)
        self.tabJajarGenjang = ttk.Frame(self.tabControl)
        self.tabLayang_Layang = ttk.Frame(self.tabControl)
        self.tabLingkaran = ttk.Frame(self.tabControl)
        self.tabSegitiga = ttk.Frame(self.tabControl)
        self.tabTrapesium = ttk.Frame(self.tabControl)


        self.tabControl.add(self.tabPersegi, text="Persegi")
        self.tabControl.add(self.tabPersegiPanjang, text="PersegiPanjang")
        self.tabControl.add(self.tabBelahKetupat, text="BelahKetupat")
        self.tabControl.add(self.tabJajarGenjang, text="JajarGenjang")
        self.tabControl.add(self.tabLayang_Layang, text="Layang_Layang")
        self.tabControl.add(self.tabLingkaran, text="Lingkaran")
        self.tabControl.add(self.tabSegitiga, text="Segitiga")
        self.tabControl.add(self.tabTrapesium, text="Trapesium")

        self.tabControl.pack(fill="both", expand=True)

        self.aturKomponenPersegi()
        self.aturKomponenPesegiPanjang()
        self.aturKomponenBelahKetupat()
        self.aturKomponenJajarGenjang()
        self.aturKomponenLayang_Layang()
        self.aturKomponenLingkaran()
        self.aturKomponenSegitiga()
        self.aturKomponenTrapesium()

    def aturKomponenPersegi(self):
        mainFrame = Frame(self.tabPersegi, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Panjang Sisi:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.txtSisiPersegi = Entry(mainFrame)
        self.txtSisiPersegi.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuasPersegi = Entry(mainFrame)
        self.txtLuasPersegi.grid(row=1, column=1, padx=5, pady=5)
        self.txtKelilingPersegi = Entry(mainFrame)
        self.txtKelilingPersegi.grid(row=2, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', 
            command=self.onHitungPersegi)
        self.btnHitung.grid(row=3, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenPesegiPanjang(self):
        mainFrame = Frame(self.tabPersegiPanjang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Panjang:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Lebar:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtPanjang = Entry(mainFrame)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasPersegiPanjang = Entry(mainFrame)
        self.txtLuasPersegiPanjang.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelilingPersegiPanjang = Entry(mainFrame)
        self.txtKelilingPersegiPanjang.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', 
            command=self.onHitungPersegiPanjang)
        self.btnHitung.grid(row=5, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenBelahKetupat(self):
        mainFrame = Frame(self.tabBelahKetupat, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')
        
        Label(mainFrame, text='Diagonal 1:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Diagonal 2:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtDiagonal1 = Entry(mainFrame)
        self.txtDiagonal1.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiagonal2 = Entry(mainFrame)
        self.txtDiagonal2.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasBelahketupat = Entry(mainFrame)
        self.txtLuasBelahketupat.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiBelahketupat = Entry(mainFrame)
        self.txtSisiBelahketupat.grid(row=4, column=1, padx=5, pady=5)
        self.txtKelilingBelahketupat = Entry(mainFrame)
        self.txtKelilingBelahketupat.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungBelahketupat)
        self.btnHitung.grid(row=6, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenJajarGenjang(self):
        mainFrame = Frame(self.tabJajarGenjang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi A:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi B:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtAlasJajargenjang = Entry(mainFrame)
        self.txtAlasJajargenjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiJajargenjang = Entry(mainFrame)
        self.txtTinggiJajargenjang.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasJajargenjang = Entry(mainFrame)
        self.txtLuasJajargenjang.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiAJajargenjang = Entry(mainFrame)
        self.txtSisiAJajargenjang.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiBJajargenjang = Entry(mainFrame)
        self.txtSisiBJajargenjang.grid(row=5, column=1, padx=5, pady=5)
        self.txtKelilingJajargenjang = Entry(mainFrame)
        self.txtKelilingJajargenjang.grid(row=6, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungJajargenjang)
        self.btnHitung.grid(row=7, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')
    
    def aturKomponenLayang_Layang(self):
        mainFrame = Frame(self.tabLayang_Layang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Diagonal 1:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Diagonal 2:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        self.txtDiagonal1Layanglayang = Entry(mainFrame)
        self.txtDiagonal1Layanglayang.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiagonal2Layanglayang = Entry(mainFrame)
        self.txtDiagonal2Layanglayang.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasLayanglayang = Entry(mainFrame)
        self.txtLuasLayanglayang.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelilingLayanglayang = Entry(mainFrame)
        self.txtKelilingLayanglayang.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungLayang_Layang)
        self.btnHitung.grid(row=5, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenLingkaran(self):
        mainFrame = Frame(self.tabLingkaran, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Jari-Jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=1, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=2, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungLingkaran)
        self.btnHitung.grid(row=3, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenSegitiga(self):
        mainFrame = Frame(self.tabSegitiga, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi A:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi B:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi C:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)

        self.txtAlas = Entry(mainFrame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiA = Entry(mainFrame)
        self.txtSisiA.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiB = Entry(mainFrame)
        self.txtSisiB.grid(row=5, column=1, padx=5, pady=5)
        self.txtSisiC = Entry(mainFrame)
        self.txtSisiC.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungSegitiga)
        self.btnHitung.grid(row=8,column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def aturKomponenTrapesium(self):
        mainFrame = Frame(self.tabTrapesium, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='lightblue')

        Label(mainFrame, text='Panjang Sisi Atas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Panjang Sisi Bawah:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi Kanan Atas:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi Kanan Bawah:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)

        self.txtSisiAtas = Entry(mainFrame)
        self.txtSisiAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtSisiBawah = Entry(mainFrame)
        self.txtSisiBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiKananAtas = Entry(mainFrame)
        self.txtSisiKananAtas.grid(row=5, column=1, padx=5, pady=5)
        self.txtSisiKananBawah = Entry(mainFrame)
        self.txtSisiKananBawah.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungTrapesium)
        self.btnHitung.grid(row=8, column=1,padx=5,pady=5)
        self.btnHitung.configure(bg='lightgreen')

    def onHitungPersegi(self):
        sisi = float(self.txtSisiPersegi.get())
        luas = sisi * sisi
        keliling = 4 * sisi
        self.txtLuasPersegi.delete(0, END)
        self.txtLuasPersegi.insert(END, str(luas))
        self.txtKelilingPersegi.delete(0, END)
        self.txtKelilingPersegi.insert(END,str(keliling))

    def onHitungPersegiPanjang(self):
        panjang = float(self.txtPanjang.get())
        lebar = float(self.txtLebar.get())
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        self.txtLuasPersegiPanjang.delete(0, END)
        self.txtLuasPersegiPanjang.insert(END, str(luas))
        self.txtKelilingPersegiPanjang.delete(0, END)
        self.txtKelilingPersegiPanjang.insert(END,str(keliling))

    def onHitungBelahketupat(self):
        diagonal1 = float(self.txtDiagonal1.get())
        diagonal2 = float(self.txtDiagonal2.get())
        luas = 0.5 * diagonal1 * diagonal2
        sisi = math.sqrt(0.5 * (diagonal1 ** 2 + diagonal2 ** 2))
        keliling = 4 * sisi
        self.txtLuasBelahketupat.delete(0, END)
        self.txtLuasBelahketupat.insert(END, str(luas))
        self.txtSisiBelahketupat.delete(0, END)
        self.txtSisiBelahketupat.insert(END, str(sisi))
        self.txtKelilingBelahketupat.delete(0, END)
        self.txtKelilingBelahketupat.insert(END,str(keliling))

    def onHitungJajargenjang(self):
        alas = float(self.txtAlasJajargenjang.get())
        tinggi = float(self.txtTinggiJajargenjang.get())
        sisi_a = float(self.txtSisiAJajargenjang.get())
        sisi_b = float(self.txtSisiBJajargenjang.get())
        luas = alas * tinggi
        keliling = 2 * (sisi_a + sisi_b)
        self.txtLuasJajargenjang.delete(0, END)
        self.txtLuasJajargenjang.insert(END, str(luas))
        self.txtKelilingJajargenjang.delete(0, END)
        self.txtKelilingJajargenjang.insert(END,str(keliling))

    def onHitungLayang_Layang(self):
        diagonal1 = float(self.txtDiagonal1Layanglayang.get())
        diagonal2 = float(self.txtDiagonal2Layanglayang.get())
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (math.sqrt((0.25 * diagonal1 ** 2) + (0.25 * diagonal2 ** 2)))
        self.txtLuasLayanglayang.delete(0, END)
        self.txtLuasLayanglayang.insert(END, str(luas))
        self.txtKelilingLayanglayang.delete(0, END)
        self.txtKelilingLayanglayang.insert(END,str(keliling))

    def onHitungLingkaran(self):
        jari_jari = float(self.txtJariJari.get())
        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onHitungSegitiga(self):
        alas = float(self.txtAlas.get())
        tinggi = float(self.txtTinggi.get())
        sisi_a = float(self.txtSisiA.get())
        sisi_b = float(self.txtSisiB.get())
        sisi_c = float(self.txtSisiC.get())
        luas = 0.5 * alas * tinggi
        keliling = sisi_a + sisi_b + sisi_c
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))
    def onHitungTrapesium(self):
        sisi_atas = float(self.txtSisiAtas.get())
        sisi_bawah = float(self.txtSisiBawah.get())
        tinggi = float(self.txtTinggi.get())
        sisi_kanan_atas = float(self.txtSisiKananAtas.get())
        sisi_kanan_bawah = float(self.txtSisiKananBawah.get())
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        keliling = sisi_atas + sisi_bawah + sisi_kanan_atas + sisi_kanan_bawah
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END,str(keliling))
    
    def onKeluar(self):
        self.parent.destroy()

if __name__== '__main__':
    root = Tk()
    aplikasi = AplikasiLuasBangun(root)
    root.mainloop()