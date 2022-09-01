import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1200x628")

menu = ImageTk.PhotoImage(Image.open("apex_screen.jpg"))
menuimage = tk.Label(root,image = menu)

menuimage.pack()