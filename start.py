from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import tkinter as tk
import webbrowser
#from choice import selection
#from mmm import *
from detect import detectuh,get_model_instance_segmentation


    
def tutorials():
    webbrowser.open('http://srisharaan.github.io/mmm')


def startuh():
    def pred():
        temp=e1.get()
        detectuh(temp)


        
    IMAGE_PATH ='C:/Users/srisharaan/Desktop/face mask/mmmbg.png'
    WIDTH, HEIGTH = 600, 400

    rot = tk.Tk()
    rot.geometry('{}x{}'.format(WIDTH, HEIGTH))
    rot.title("Face Mask Detector")
    rot.configure(bg="#99643A")
    #bg = PhotoImage(file = IMAGE_PATH) 
  
    # Show image using label 
    #label1 = Label( rot, image = bg) 
    #label1.place(x = 0, y = 0) 

    #canvas = tk.Canvas(rot, width=WIDTH, height=HEIGTH)
    
    #img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    #canvas.background = img  # Keep a reference in case this code is put in a function.
    #bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
    #myFont = font.Font(family='Tw Cen MT', size=16)
    #canvas.pack()


    
    mylabel1=Label(rot,text="Image Location",bg="#99643A",fg='white')
    mylabel1.grid(row=3,column=0)
    loca = tk.StringVar()

    e1 = Entry(rot, width=35, borderwidth=5,textvariable = loca)
    e1.grid(row=3, column=1,sticky="ew")
    button_2 = Button(rot, text="OK", padx=20, pady=10, command=pred,bg="#99643A",fg='white')
    button_2.grid(row=10, column=1)
    rot.mainloop()

    
    
#    root.destroy()
#    #button4= tk.Button(root, text="finding your hotword",bg="#99643A",fg='white')
 #   #button_window4 = canvas.create_window(200, 300, anchor=tk.NW, window=button4)
  #  #button4['font'] = myFont
   # selection()
    ##a=selectioney()
    ##print(a)
    
def aboutuh():
    #root.destroy()
    slave=Tk()
    slave['background']='#99643A'
    slave.title("Face mask Detection")
    myFont = font.Font(family='Tw Cen MT', size=16)
    mylabel1=Label(slave,text="Face mask detector \n"
                   "This application is able to detect whether a person has worn a mask or not \n "
                   "\n"
                   "\n"
                   "\n"
                   "Developed by-Srisharaan S,Pavan Kumar P,Vinothraj R \n"
                   "\n"
                   "\n"
                   "\n"
                   "Thank you so much for using our application",bg='#99643A',fg='white')
    
    mylabel1.grid(row=3,column=0)
    slave.mainloop()
#def donateuh():
#    #root.destroy()
 #  slave.geometry("500x500")
  #  slave['background']='#99643A'
   # slave.title("MMM")
    #myFont = font.Font(family='Tw Cen MT', size=16)
    #mylabel1=Label(slave,text="Support my work by buying me a Biryani \n",bg='#99643A',fg='white')
    #mylabel1.pack()
    #photo=PhotoImage(file="qr.png")
    #label=Label(slave,image=photo)
    #label.pack()

    #slave.mainloop()
    
    
    

IMAGE_PATH = 'mmmbg.png'
WIDTH, HEIGTH = 600, 400

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGTH))
root.title("Face Mask Detector")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)



myFont = font.Font(family='Tw Cen MT', size=16)

# Put a tkinter widget on the canvas.
button = tk.Button(root, text="Start",bg="#99643A",fg='white',command=startuh)
button_window = canvas.create_window(15, 20, anchor=tk.NW, window=button)
button['font'] = myFont


button2 = tk.Button(root, text="Tutorials",bg="#99643A",fg='white',command=tutorials)
button_window2 = canvas.create_window(500, 20, anchor=tk.NW, window=button2)
button2['font'] = myFont


button3 = tk.Button(root, text="About",bg="#99643A",fg='white',command=aboutuh)
button_window3 = canvas.create_window(15, 300, anchor=tk.NW, window=button3)
button3['font'] = myFont

#button4= tk.Button(root, text="Donate",bg="#99643A",fg='white',command=donateuh)
#button_window4 = canvas.create_window(500, 300, anchor=tk.NW, window=button4)
#button4['font'] = myFont


root.mainloop()
