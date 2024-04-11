#import random
#from tkinter import *
#from random import randint
#import time
#import threading
#
#root = Tk()
#root.attributes("-alpha", 0)
#root.overrideredirect(1)
#root.attributes("-topmost", 1)
#
#def placewindows():
#    while True:
#        win = Toplevel(root)
#        win.geometry("450x450+{}+{}".format(str(randint(0, root.winfo_screenwidth() - 500)), str(randint(0, root.winfo_screenheight() - 500))))
#        win.overrideredirect(1)
#        Label(win, text ="looooooooooooooool!", fg="red").place(relx=.38, rely=.3)
#        win.lift()
#        win.attributes("-topmost", True)
#        win.attributes("-topmost", False)
#        root.lift()
#        root.attributes("-topmost", True)
#        root.attributes("-topmost", False)
#
#
#threading.Thread(target=placewindows).start()
#
#root.mainloop()


##start av crypto kod##

#from cryptography.fernet import Fernet


#def generate_key():
#    key = Fernet.generate_key()
#    with open("nyckel", "wb") as key_file:
#        key_file.write(key)
#
#def load_key():
#    return open("nyckel", "rb").read()
#
#def encryption_message(message, key):
#    encoded_message = message.encode()
#    f = Fernet(key)
#    encryption_message = f.encrypt(encoded_message)
#    return encoded_message
#
#def encryption_message(message, key):
#    encoded_message = message.encode()
#    f = Fernet(key)
#    encryption_message = f.decrypt(encoded_message)
#    return decoded_message.decode()


#message = input("message pls: ").lower()
#key = int(input("shift nr? "))




##if key == 0:
##    new = alphabet
##elif key > 0:
##    one = alphabet[:key]
##    two = alphabet[key:]
##    new = two + one
##
##encrypted = ""
##
##for char in message:
##    if char == '':
##        encrypted += ""
##    else:
##        for i in range(len(new)):
##            if char == alphabet[i]:
##                encrypted += new[i]
##                break
##        else:
##            encrypted += char
#
#
##for  in range(len(message)):
##    if message[i] == 0:
##        encrypted += ""
##    for i in range(len(new)):
##        if message[i] == alphabet[i]:
##            encrypted == new[i]
#
##print(encrypted)


from cryptography.fernet import Fernet


def Encrypt(message, key):
    if key == 0:
        new = alphabet
    elif key > 0:
        one = alphabet[:key]
        two = alphabet[key:]
        new = two + one
    
    encrypted = ""

    for char in message:
        if char == '':
            encrypted += " "
        else :
            for i in range(len(new)):
                if char == alphabet[i]:
                    encrypted += new[i]
                    break
            else:
                encrypted += char

    return encrypted

def Decrypt(encrypted_message, key):
    decrypted = ""
    for char in encrypted_message:
        if char == ' ':
            decrypted += " "
        else:
            index = alphabet.find(char)
            decrypted_char_index = (index - key) % len(alphabet)
            decrypted += alphabet[decrypted_char_index]
    return decrypted



def kola(medelande, nyckel):
    kola = ""
    for char in medelande:
        if char == ' ':
            kola += " "
        else:
            index = alphabet.find(char)
            kola_char_index = (index - nyckel) % len(alphabet)
            kola += alphabet[kola_char_index]
    return kola

alphabet = "abcdefghijklmnopqrstuvwxyz"

answer = input("Encrypt or Decrypt: ").lower()

x = ""

if answer == "encrypt":
    message = input("message pls: ").lower()
    key = int(input("shift nr? "))
    x = "yes"
elif answer == "decrypt":
    medelande = input("message pls: ").lower()
    nyckel = int(input("shift nr? "))
    x = "no"
else:
    print("U Smort")


if x == "yes":
    encrypted_message = Encrypt(message, key)
    print("Encrypted: ", encrypted_message)

    dencrypted_message = Decrypt(encrypted_message, key)
    print("Decrypted: ", dencrypted_message)

elif x == "no":
    fan = kola(medelande, nyckel)
    print("Decrypted: ", fan)


