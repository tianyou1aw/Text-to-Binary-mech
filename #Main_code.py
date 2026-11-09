#Main_code.py
import tkinter as tk

def Binary():
    global final_result
    final_result = ""
    entrybox = Entry.get()
    for letter in entrybox:
        id = ord(letter)
        binary_letter = format(id, '08b')
        final_result = final_result + binary_letter + " "
        MainLabel.config(text=f"{final_result}")


root = tk.Tk()
MainLabel = tk.Label(root, text=f"")
Title = tk.Label(root, text=f"Text to Binary")
Entry = tk.Entry(root)
Button = tk.Button(root, text=f"Turn to Binary", command=Binary)



Title.pack()

Entry.pack()
Button.pack()
MainLabel.pack()
root.mainloop()
