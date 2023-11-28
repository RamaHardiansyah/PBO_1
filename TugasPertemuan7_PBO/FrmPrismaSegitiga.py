from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPrismaSegitiga:
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
        Label(mainFrame, text='alas_segitiga:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="tinggi_segitiga:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="tinggi_prisma").grid(row=2, column=0, 
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtalas_segitiga = Entry(mainFrame) 
        self.txtalas_segitiga.grid(row=0, column=1, padx=5, pady=5)  
        self.txttinggi_segitiga = Entry(mainFrame) 
        self.txttinggi_segitiga.grid(row=1, column=1, padx=5, pady=5) 
        self.txttinggi_prisma = Entry(mainFrame) 
        self.txttinggi_prisma.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume Prisma Segitiga 
    def onHitung(self, event=None):
        alas_segitiga = int(self.txtalas_segitiga.get())
        tinggi_segitiga = int(self.txttinggi_segitiga.get())
        tinggi_prisma = int(self.txttinggi_prisma.get())
        l = ((alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga))
        V = (0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(l))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(l))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaSegitiga(root, "Program Luas PrismaSegitiga")
    root.mainloop() 