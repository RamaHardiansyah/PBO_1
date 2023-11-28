from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimpat:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='sisi_alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="tinggi_limas:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="tinggi_segitiga").grid(row=2, column=0, 
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtsisi_alas = Entry(mainFrame) 
        self.txtsisi_alas.grid(row=0, column=1, padx=5, pady=5)  
        self.txttinggi_limas = Entry(mainFrame) 
        self.txttinggi_limas.grid(row=1, column=1, padx=5, pady=5) 
        self.txttinggi_segitiga = Entry(mainFrame) 
        self.txttinggi_segitiga.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume Limpat
    def onHitung(self, event=None):
        sisi_alas = int(self.txtsisi_alas.get())
        tinggi_limas = int(self.txttinggi_limas.get())
        tinggi_segitiga = int(self.txttinggi_segitiga.get())
        l = ((sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga))
        V = ((sisi_alas ** 2 * tinggi_limas) / 3)
        
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(l))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(l))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimpat(root, "Program Luas Limpat")
    root.mainloop() 