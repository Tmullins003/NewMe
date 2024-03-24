#notes operations
import tkinter as tk

window = tk.Tk()
label = tk.Label(text="NewME")
label.pack()
greeting = tk.Label(text="Welcome to NewMe! write your notes or make a to-do list. ")
greeting.pack()
window.mainloop()

print(input("Enter your note: "))