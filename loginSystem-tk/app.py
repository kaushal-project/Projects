# 

from tkinter import *
# using pillow lib to convert image into png
from PIL import ImageTk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        # ======= BG Image ========
        self.bg=ImageTk.PhotoImage(file="./img.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        

        # ======= Login Frame =============
        frame_login = Frame(self.root,bg="white")
        frame_login.place(x=150,y=150,height=340,width=500)

        # ====== Label Title ======================
        title = Label(frame_login,text="Login Here",font=("sans",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        # ====== Label Discription ======================
        disc = Label(frame_login,text="User Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        # ====== Label Username Entry  ======================
        lbl_user = Label(frame_login,text="Username",font=("sans",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.txt_user = Entry(frame_login,font=("times new roman",15),bg="lightgrey").place(x=90,y=170,width=350,height=35)

        # ====== Label Password ======================
        lbl_user = Label(frame_login,text="Password",font=("sans",15,"bold"),fg="grey",bg="white").place(x=90,y=200)
        self.txt_user = Entry(frame_login,font=("times new roman",15),bg="lightgrey").place(x=90,y=230,width=350,height=35)
# Object
root = Tk()
obj = Login(root)
root.mainloop()