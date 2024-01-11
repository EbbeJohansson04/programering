import random
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("450x450+{}+{}".format(str(randint(0, root.winfo_screenwidth() - 500)), str(randint(0, root.winfo_screenheight() - 500))))
        win.overrideredirect(1)
        Label(win, text ="looooooooooooooool!", fg="red").place(relx=.38, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)


threading.Thread(target=placewindows).start()

root.mainloop()






