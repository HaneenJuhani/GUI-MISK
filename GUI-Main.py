import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter.constants import W 

root = tk.Tk()

canvas = tk.Canvas(root, height=650, width=1300, bg="#263D42")
canvas.pack()


# frames of the app

frame1 = tk.Frame(root, bg="#F3F3F3")
frame1.place(relwidth=0.5, relheight=0.35, relx=0.07, rely=0.07)

frame2 = tk.Frame(root, bg="#F3F3F3")
frame2.place(relwidth=0.5, relheight=0.35, relx=0.07, rely=0.55)

frame3 = tk.Frame(root, bg="#F3F3F3")
frame3.place(relwidth=0.1, relheight=0.05, relx=0.47, rely=0.44)

frame4 = tk.Frame(root, bg="#F3F3F3")
frame4.place(relwidth=0.33, relheight=0.2, relx=0.65, rely=0.15)

frame5 = tk.Frame(root, bg="#F3F3F3")
frame5.place(relwidth=0.33, relheight=0.2, relx=0.65, rely=0.65)

frame6 = tk.Frame(root, bg="#F3F3F3")
frame6.place(relwidth=0.1, relheight=0.05, relx=0.47, rely=0.92)





root.mainloop()