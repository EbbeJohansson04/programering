import random
from tkinter import *
from tkinter import Toplevel
from random import randint
from PIL import Image, ImageTk

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("450x450+{}+{}".format(str(randint(0, root.winfo_screenwidth() - 500)), str(randint(0, root.winfo_screenheight() - 500))))
        win.overrideredirect(1)
        
        # Open the image with PIL and convert it to Tkinter PhotoImage
        img = Image.open("Trollface_non-free.png")
        img_tk = ImageTk.PhotoImage(img)
        
        # Use a Label to display the image
        label = Label(win, image=img_tk)
        label.image = img_tk
        label.place(relx=.38, rely=.3)
        
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)

placewindows()  # Call the function directly in the main thread

root.mainloop()
