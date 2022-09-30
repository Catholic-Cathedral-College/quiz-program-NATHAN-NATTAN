import tkinter as tk
from PIL import Image, ImageTk
#center of the GUI
root = tk.Tk()
# make the boundery this size
root.geometry("600x313")

score = 0 


#this is to  identify each page

menu1 = tk.Frame(root, width=600, height=338)
image2 = tk.Frame(root, width=600, height=313)
image3 = tk.Frame(root, width=600, height=313)
image4 = tk.Frame(root, width=600, height=313)
image5 = tk.Frame(root, width=600, height=313)
image6 = tk.Frame(root, width=600, height=313)

#line 14 says find "apex_screen.jpg" in the Files
menu = ImageTk.PhotoImage(Image.open("image1.jpg"))
menuimage = tk.Label(menu1, image=menu)

#pack is a line to say pack all of this in the screen
menuimage.pack()

#this line is for the button it says to erase the fist image
def play():
   menu1.forget()
   start.destroy()
   image2.pack() 

def play2():
   image2.forget()
   image3.pack()
    
def play3():
   image3.forget()
   image4.pack()
   
def play4():
   image4.forget()
   image5.pack()

def play5():
   image5.forget()
   image6.pack()

def play6():
   image6.forget()
   image7.pack()
#This it the buttons 
startbutton = ImageTk.PhotoImage(Image.open("Start.jpg"))
canvas1 = tk.Canvas(menu1, width=50, height=50,)
start = tk.Button(text="start the test", image=startbutton, command=play)
start.configure(width= 103, height= 50)
start_window = canvas1.create_window(40, 50)

start.place(x=155, y=125)
menu1.pack()


#this is the next frame 
frame1 = ImageTk.PhotoImage(file="image2.jpg")
quiz_page1 = tk.Label(image2, image=frame1)
canvas = tk.Canvas(image2, width=600, height=367)
canvas.pack(fill='both')
canvas.create_image(298, 158, image=frame1)

#next button 
nextb=ImageTk.PhotoImage(Image.open("next.jpg"))
canvas2 = tk.Canvas(image2, width=50, height=50)
next = tk.Button(image2, text="start the test", image=nextb, command=play2)
next.configure(width=100)
next_WINDOW = canvas2.create_window(30, 40)
next.place(x=460, y=259)
image2.pack()

frame2 = ImageTk.PhotoImage(file="image3.jpg")
quiz_page2 = tk.Label(image3, image=frame2)
canvas = tk.Canvas(image3, width=600, height=367)
canvas.pack(fill='both')
canvas.create_image(298, 158, image=frame2)
image3.pack()

question1=ImageTk.PhotoImage(Image.open("q1.jpg"))
canvas3 = tk.Canvas(image3, width=250, height=105)
q1 = tk.Button(image3, text="start", image= question1, command=play3)
q1.configure(width=250)
q1_window = canvas3.create_window(30,40)
q1.place(x=250, y=70)

question2=ImageTk.PhotoImage(Image.open("q2.jpg"))
canvas4 = tk.Canvas(image3, width=250, height=105)
q2 = tk.Button(image3, text="start", image= question2, command=play3)
q2.configure(width=250)
q2_window = canvas4.create_window(30,40)
q2.place(x=320, y=185)

frame3 = ImageTk.PhotoImage(file="image4.jpg")
quiz_page3 = tk.Label(image4, image=frame3)
canvas = tk.Canvas(image4, width=600, height=367)
canvas.pack(fill='both')
canvas.create_image(298, 158, image=frame3)
image4.pack()

question3=ImageTk.PhotoImage(Image.open("q3.jpg"))
canvas5 = tk.Canvas(image4, width=250, height=105)
q3 = tk.Button(image4, text="start", image= question3, command=play4)
q3.configure(width=250)
q3_window = canvas5.create_window(30,40)
q3.place(x=320, y=185)

question4=ImageTk.PhotoImage(Image.open("q4.jpg"))
canvas6 = tk.Canvas(image4, width=250, height=105)
q4 = tk.Button(image4, text="start", image= question4, command=play4)
q4.configure(width=250)
q4_window = canvas6.create_window(30,40)
q4.place(x=250, y=70)

frame4 = ImageTk.PhotoImage(file="image5.jpg")
quiz_page4 = tk.Label(image5, image=frame4)
canvas = tk.Canvas(image5, width=600, height=367)
canvas.pack(fill='both')
canvas.create_image(298, 158, image=frame4)
image5.pack()

question5=ImageTk.PhotoImage(Image.open("q5.jpg"))
canvas7 = tk.Canvas(image5, width=250, height=105)
q5 = tk.Button(image5, text="start", image= question5, command=play5)
q5.configure(width=100)
q5_window = canvas7.create_window(30,40)
q5.place(x=320, y=185)

question6=ImageTk.PhotoImage(Image.open("q6.jpg"))
canvas8 = tk.Canvas(image5, width=250, height=105)
q6 = tk.Button(image5, text="start", image= question6, command=play5)
q6.configure(width=100)
q6_window = canvas8.create_window(30,40)
q6.place(x=400, y=70)

frame5 = ImageTk.PhotoImage(file="image6.jpg")
quiz_page4 = tk.Label(image6, image=frame5)
canvas = tk.Canvas(image6, width=600, height=367)
canvas.pack(fill='both')
canvas.create_image(298, 158, image=frame5)
image6.pack()

question7=ImageTk.PhotoImage(Image.open("q7.jpg"))
canvas9 = tk.Canvas(image6, width=250, height=105)
q7 = tk.Button(image6, text="start", image= question7, command=play6)
q7.configure(width=250)
q7_window = canvas9.create_window(30,40)
q7.place(x=250, y=70)

question8=ImageTk.PhotoImage(Image.open("q8.jpg"))
canvas10 = tk.Canvas(image6, width=250, height=105)
q8 = tk.Button(image6, text="start", image= question8, command=play6)
q8.configure(width=250)
q8_window = canvas10.create_window(30,40)
q8.place(x=320, y=185)

