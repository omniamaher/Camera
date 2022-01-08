from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from db import Database
import pymysql
import tkinter as tk
class home:
   

    def register_employee(self):
        self.root.destroy()
        import register_employee

    def view_camera(self):
     self.root.destroy()
     import view_camera

    def __init__(self,root):
        self.root=root
        self.root.title("PANOPTES")
        self.root.geometry("1000x580")
        #back ground color #
        self.root.config(bg="white")
        self.root.resizable(False, False)
        #back ground image#
        self.bg=ImageTk.PhotoImage(file="scamera.jpeg")
        bg=Label(self.root,image=self.bg).place(x=0,y=-10,width=450,height=600)
        #register frame#
        frame1=Frame(self.root,bg="white")
        frame1.place(x=500,y=150,width=400,height=500)
        #logo
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='panoptes.png'))

        #register employees button 
        regemp_btn = Button(frame1,command=self.register_employee,text='Regiser Employees',fg="chocolate2",height="5",width=20,cursor="hand").place(x=150,y=200)

        #view camera button 
        camera_btn = Button(frame1,command=self.view_camera,bg="white",font=30,text='view camera',height="5",width=20,cursor="hand",fg="chocolate2").place(x=150,y=50)
        logout=Button(frame1,text="Log Out",command=self.logout,cursor="hand",fg='Red',width=9).place(x=200,y=400)
    def logout(self):
        self.root.destroy()
        import login_screen

     



root=Tk()
obj=home(root)
root.mainloop()