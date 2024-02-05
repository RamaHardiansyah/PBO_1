from tkinter import Frame, Label, Entry, Button, ttk, BOTH, END, Tk, StringVar, messagebox
from apotek import Apotek

class Formapotek:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=True)
        
        # Label
        Label(mainFrame, text='Kdobat:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.txtkdobat = Entry(mainFrame) 
        self.txtkdobat.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkdobat.bind("<Return>", self.onCari)  # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Berat:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.txtberat = Entry(mainFrame) 
        self.txtberat.grid(row=2, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Bentuk:').grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.bentuk = StringVar()
        Cbo = ttk.Combobox(mainFrame, width=27, textvariable=self.bentuk) 
        Cbo.grid(row=3, column=1, padx=5, pady=5)
        Cbo['values'] = ('kapsul', 'tablet', 'sirup')
        Cbo.current(0)      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btncari = Button(mainFrame, text='Cari', command=self.onCari, width=10)
        self.btncari.grid(row=3, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kdobat', 'nama', 'berat', 'bentuk')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kdobat', text='Kdobat')
        self.tree.column('kdobat', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('berat', text='Berat')
        self.tree.column('berat', width="50")
        self.tree.heading('bentuk', text='Bentuk')
        self.tree.column('bentuk', width="100")
        # set tree position
        self.tree.grid(row=4, columnspan=4)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtkdobat.delete(0, END)
        self.txtkdobat.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")       
        self.txtberat.delete(0, END)
        self.txtberat.insert(END, "")   
        self.bentuk.set("")
        self.btnSimpan.config(text="Simpan")
    
    # Menghapus semua pilihan pada Treeview
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.onReload()
        self.ditemukan = False

        
    def onReload(self, event=None):
        # get data obat
        obat = Apotek()
        result = obat.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        obats = []
        for row_data in result:
            obats.append(row_data)

        for obat in obats:
            self.tree.insert('', END, values=obat)
    
    def onCari(self, event=None):
        kdobat = self.txtkdobat.get()
        obat = Apotek()
        res = obat.getBykdobat(kdobat)
        rec = obat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        kdobat = self.txtkdobat.get()
        obat = Apotek()
        res = obat.getBykdobat(kdobat)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, obat.nama)
        self.txtberat.delete(0, END)
        self.txtberat.insert(END, obat.berat) 
        self.bentuk.set(obat.bentuk_obat)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kdobat = self.txtkdobat.get()
        nama = self.txtNama.get()
        berat = self.txtberat.get() 
        bentuk = self.bentuk.get()
        
        obat = Apotek()
        obat.kdobat = kdobat
        obat.nama = nama
        obat.berat = berat
        obat.bentuk_obat = bentuk
        
        if self.ditemukan:
            res = obat.updateBykdobat(kdobat)
            ket = 'Diperbarui'
        else:
            res = obat.simpan()
            ket = 'Disimpan'
            
        rec = obat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kdobat = self.txtkdobat.get()
        obat = Apotek()
        obat.kdobat = kdobat
        if self.ditemukan:
            res = obat.deleteBykdobat(kdobat)
            rec = obat.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = Formapotek(root, "Aplikasi Data Apotek")
    root.mainloop()
