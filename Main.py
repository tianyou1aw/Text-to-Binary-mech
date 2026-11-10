"""
Main.py

"""

import tkinter as tk

def convert_to_binary():
    final_result = ""
    entrybox = insert_entry.get()
    for letter in entrybox:
        id = ord(letter)
        binary_letter = format(id, '08b')
        final_result = final_result + binary_letter + " "
    Main_Label.config(text=f"{final_result}")


root = tk.Tk()
Main_Label = tk.Label(root, text=f"")
title_label = tk.Label(root, text=f"Text to Binary")
insert_entry = tk.Entry(root)
binary_converter = tk.Button(root, text=f"Turn to Binary", command=convert_to_binary)



title_label.pack()

insert_entry.pack()
binary_converter.pack()
Main_Label.pack()
root.mainloop()
