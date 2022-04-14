from tkinter import *
from tkinter import ttk


def AyarlarıYukle():
    return

def AyarlarıKaydet():
    return

def calculate(*args):
    try:
        value = float(args.feet.get())
        args.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

isFullscreen = False
def toggleFullscreen():
    global isFullscreen
    root.attributes("-fullscreen", not isFullscreen)
    isFullscreen = (isFullscreen == False)

root = Tk("Classy" )
root.geometry("800x600")

mainframe = ttk.Frame(root, padding = "3 3 3 3")
mainframe.grid(column=0, row=0, sticky="nwse")
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

tabControl = ttk.Notebook(mainframe)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text="AnaGörünüm")
tabControl.add(tab2, text="Önizleme")
tabControl.add(tab3, text="Ayarlar")
tabControl.pack(expand=1,fill="both")


programdatafilename = StringVar()

ttk.Button(tab3, text="TamEkran", command=toggleFullscreen).grid(column=1, row=1)

ttk.Entry(tab3, width=7, textvariable=programdatafilename).grid(column=1, row=2, sticky="we")


root.mainloop()