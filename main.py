import tkinter as tk
from PIL import Image, ImageTk
#center of the GUI
root = tk.Tk()
# make the boundery this size
root.geometry("600x313")

menu = ImageTk.PhotoImage(Image.open("apex_screen.jpg"))
menuimage = tk.Label(root,image = menu)

menuimage.pack()
#diffining frame
beginimage = tk.Frame(root,width=600, height=313)
quiz_page = tk.Frame(root,width=600, height=313)


begin_image = ImageTk.PhotoImage(Image.open("button.png"))
#to erase and put another baround image 
def play():
   menuimage.forget()
   play_button.destroy()
   quiz_page.pack()


#button
canvas1 = tk.Canvas(beginimage, width=50, height=50)
play_button = tk.Button(text = "start the test", image = begin_image,command=play)
play_button.configure(width=201)
play_button_window = canvas1.create_window(30,40)

play_button.place(x=90, y=200)
print("running")
beginimage.pack()

#next frame
main = tk.PhotoImage(Image.open("writh.png"))

quiz1image = tk.Label(quiz_page,image = wraith)


quiz_page.pack()


