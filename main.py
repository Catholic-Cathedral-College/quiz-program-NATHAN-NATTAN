import tkinter as tk
from PIL import Image, ImageTk
#center of the GUI
root = tk.Tk()
# make the boundery this size
root.geometry("600x313")

#idetify 
button2 = tk.Frame(root,width=600, height=313)
button = tk.Frame(root,width=600, height=313)
wraith1 = tk.Frame(root,width=600, height=313)
mirage1 = tk.Frame(root,width=600, height=313)
#first frame 
menu = ImageTk.PhotoImage(Image.open("apex_screen.jpg"))
menuimage = tk.Label(button,image = menu)

#pack
menuimage.pack()


#to erase or put images 
def play():
   button.forget()
   play_button.destroy()
   wraith1.pack()
   mirage1.pack()
  
#button
apex_button = ImageTk.PhotoImage(Image.open("button.png"))
canvas1 = tk.Canvas(button, width=50, height=50)
play_button = tk.Button(text = "start the test", image = apex_button,command=play)
play_button.configure(width=201)
play_button_window = canvas1.create_window(30,40)

play_button.place(x=90, y=200)
print("running")
button.pack()

#next frame
wraith = ImageTk.PhotoImage(file = "writh.png")

quiz_page = tk.Label(wraith1,image = wraith) 
canvas = tk.Canvas(wraith1, width = 600, height = 313)
canvas.pack(fill='both')
canvas.create_image(298,158, image=wraith)

quiz_page.pack()
#---------------------------------------------------------------------------
