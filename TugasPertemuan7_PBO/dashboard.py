import tkinter as tk
from tkinter import Menu

from FrmBalok import *
from FrmKerucut import *
from FrmTabung import *
from FrmPrismaSegitiga import *
from FrmLimasSegitiga import *
from FrmLimpat import *
from FrmKubus import *
from FrmBola import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas dan volume Balok", FrmBalok)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas dan volume Kerucut", FrmKerucut)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Luas dan volume Tabung", FrmTabung)
)
app_menu.add_command(
    label='App PrismaSegitiga', command= lambda: new_window("Luas dan volume PrismaSegitiga", FrmPrismaSegitiga)
)
app_menu.add_command(
    label='App LimasSegitiga', command= lambda: new_window("Luas dan volume LimasSegitiga", FrmLimasSegitiga)
)
app_menu.add_command(
    label='App Limpat', command= lambda: new_window("Luas dan volume Limpat", FrmLimpat)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas dan volume Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas dan volume Bola", FrmBola)
)


def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()