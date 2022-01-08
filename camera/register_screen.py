from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from db import Database
import re
import pymysql
import re
from validate_email import validate_email
import tkinter as tk


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("PANOPTES")
        self.root.geometry("1000x580")
        self.root.resizable(False, False)
        #back ground color #
        self.root.config(bg="white")
        #back ground image#
        self.bg=ImageTk.PhotoImage(file="scamera.jpeg")
        bg=Label(self.root,image=self.bg).place(x=0,y=-10,width=300,height=600)
        #register frame#
        frame1=Frame(self.root,bg="white")
        frame1.place(x=350,y=50,width=600,height=500)
        title=Label(frame1,text="Register",font=("times new roman",20,"bold"),bg="chocolate2",fg="white").place(x=250,y=30)
        #logo
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='panoptes.png'))

        
        
        #name label and entry
        name=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=60,y=100)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=50,y=130,width=230)

        #phone label and entry
        phone=Label(frame1,text="Phone Number",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=320,y=100)
        self.txt_phone=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_phone.place(x=320,y=130,width=230)

        #address label and entry
        address=Label(frame1,text="Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_address=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_address.place(x=50,y=200,width=230)
        
        #national id label and entry
        nid=Label(frame1,text="National ID number",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=320,y=170)
        self.txt_nid=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_nid.place(x=320,y=200,width=230)

        #password and confirm password
     
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=250)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=50,y=270,width=230)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=320,y=250)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_cpassword.place(x=320,y=270,width=230)

        #job position
        self.position=Label(frame1,text="Position ",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=320)
        self.position=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.position['values']=("select","Owner","Employee","Security") 
        self.position.place(x=50,y=345,width=230)
        self.position.current(0)


        #email 
        email=Label(frame1,text="Email ",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=320,y=320)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=320,y=340,width=230)

        #register button
        register_btn = Button(frame1,text='Register',width=12,fg="chocolate2",command=self.register_data,cursor="hand").place(x=50,y=390)

        #login button 
        login_btn = Button(frame1,command=self.login_window,text='Already a user?Log in',fg="chocolate2",width=15,cursor="hand").place(x=320,y=390)

    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_address.delete(0,END)
        self.txt_nid.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_email.delete(0,END)
        self.position.current(0)

    def login_window(self):
        self.root.destroy()
        import login_screen

    def special_match(self,strg, search=re.compile(r'[^a-zA-Z.]').search):
        return not bool(search(strg))

    def num_match(self,strg, search=re.compile(r'[^0-9.]').search):
        return not bool(search(strg))



    def register_data(self):
        if self.txt_name.get()=="" or self.txt_phone.get()=="" or self.txt_address.get()=="" or self.txt_nid.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.position.get()=="select" or self.txt_email.get()=="":
            messagebox.showerror("ERROR","all field are required",parent=self.root)

        elif self.txt_password.get()!=self.txt_cpassword.get() or len(self.txt_password.get())<8:
            messagebox.showerror("ERROR","password and confirm password do not match , Password Must be atleast 8 characters long",parent=self.root)
        if self.special_match(self.txt_name.get())==False :
            messagebox.showinfo("Error!", "Name should only have Characters")
        elif validate_email(self.txt_email.get()) == False :
            messagebox.showerror("Error", "Please enter valid email(e.g.example@example.com)")
        elif len(self.txt_phone.get())<11 or self.num_match(self.txt_phone.get())==False   :
            messagebox.showerror("Error!", "Mobile should contain only numbers and should be 11 numbers ")
        elif len(self.txt_nid.get())<14 or self.num_match(self.txt_nid.get())==False   :
            messagebox.showerror("Error!", "National ID should contain only numbers and should be 14 numbers ")
        # elif len(self.txt_password.get())<8:
        #     messagebox.showinfo("Error!", "Password Must be atleast 8 characters long")
        else :
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from Employees where nid=%s",self.txt_nid.get())
                row=cur.fetchone() 
                #  print(row)
                if row!=None:
                    messagebox.showerror("Error","Employee already exists",parent=self.root)
                else:
                    cur.execute("insert into Employees (name,phone,email,position,address,nid,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.txt_name.get(),
                                        self.txt_phone.get(),
                                        self.txt_email.get(),
                                        self.position.get(),
                                        self.txt_address.get(),
                                        self.txt_nid.get(),
                                        self.txt_password.get(),    
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showerror("success","You have registered successfully",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)
        

root=Tk()
obj=register(root)
root.mainloop()
