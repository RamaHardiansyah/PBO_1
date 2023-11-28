from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from math import pi

class FrmKerucut:
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
        Label(mainFrame, text='Jari_jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="G_pelukis").grid(row=2, column=0, 
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        

        # pasang textbox
        self.txtJari_jari = Entry(mainFrame) 
        self.txtJari_jari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtG_pelukis = Entry(mainFrame) 
        self.txtG_pelukis.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 
        
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume Kerucut 
    def onHitung(self, event=None):
        j = int(self.txtJari_jari.get())
        t = int(self.txtTinggi.get())
        G_pelukis = int(self.txtG_pelukis.get())
        l = (pi * j * (j + G_pelukis))
        v = ((1/3) * pi * (j ** 2) * t)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(l))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(l))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKerucut(root, "Program Luas Kerucut")
    root.mainloop() 