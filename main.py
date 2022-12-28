import tkinter as tk

from tkinter import *

from tkinter import ttk

from functions import *

root = tk.Tk()

root.geometry("550x350")

root.title("Area Calculator")

label = ttk.Label(root, text='Dimension', font=10, foreground="#273746")
label.grid(column=0, row=0, padx=20, pady=10,  sticky='w')

label = ttk.Label(root, text='2D', font=10, foreground="#273746")
label.grid(column=0, row=0, padx=500, pady=10,  sticky='w')

root.mainloop()
