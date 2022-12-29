import tkinter as tk

from tkinter import *

from tkinter import ttk

root = tk.Tk()

root.geometry("550x350")

root.title("Area Calculator")

label = ttk.Label(root, text='Dimension', font=10, foreground="#273746")
label.grid(column=0, row=0, padx=20, pady=10,  sticky='w')

'''shape_dimensions = ["2D", "3D"]

variable = StringVar(root)
variable.set(shape_dimensions[0])

dropdown = ttk.OptionMenu(root, variable, *shape_dimensions,font=10, foreground="#273746")
dropdown.grid(column=0, row=0, padx=500, pady=10,  sticky='w')'''


label = ttk.Label(root, text='2D', font=10, foreground="#273746")
label.grid(column=0, row=0, padx=500, pady=10,  sticky='w')

root.mainloop()
