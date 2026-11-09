#Main_code.py
import tkinter as tk
import random
import time

def Binary():
    global final_result
    final_result = ""
    entrybox = Entry.get()
    for letter in entrybox:
        id = ord(letter)
        binary_letter = format(id, '08b')
        final_result = final_result + binary_letter + " "
        thelabel.config(text=f"{final_result}")


root = tk.Tk()
thelabel = tk.Label(root, text=f"")
label = tk.Label(root, text=f"Text to Binary")
Entry = tk.Entry(root)
Button = tk.Button(root, text=f"Turn to Binary", command=Binary)





Entry.pack()
Button.pack()
thelabel.pack()
root.mainloop()
