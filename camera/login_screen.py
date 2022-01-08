from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from db import Database
import pymysql
import tkinter as tk
def register_user():
    print("register")

def log_in():
    print("log in")
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("PANOPTES")
        self.root.geometry("1000x580")
        self.root.resizable(False, False)
        #back ground color #
        self.root.config(bg="white")
        #back ground image#
        self.bg=ImageTk.PhotoImage(file="scamera.jpeg")
        bg=Label(self.root,image=self.bg).place(x=0,y=-10,width=450,height=600)
        #logo
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='panoptes.png'))

        #register frame#
        frame1=Frame(self.root,bg="white")
        frame1.place(x=500,y=150,width=400,height=500)
        title=Label(frame1,text="Log In",font=("times new roman",20,"bold"),bg="chocolate2",fg="white").place(x=180,y=30)
        #name label and entry
        name=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=100)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=100,y=130,width=230)
    
        #password label and entry
     
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=190)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=100,y=220,width=230)
        
        #login button 
        login_btn = Button(frame1,command=self.login_function,text='Log in',width=12,cursor="hand",fg="chocolate2").place(x=150,y=270)


        #register button
        register_btn = Button(frame1,command=self.register_window,text='Register new account',fg="chocolate2",width=16,cursor="hand").place(x=130,y=300)

        #forget password button
        frgpsw_btn = Button(frame1,text='forgot password',command=self.forgot_password_window,fg="red",width=16,cursor="hand").place(x=130,y=330)

    def register_window(self):
        self.root.destroy()
        import register_screen

    def forgot_passwrord(self):
        if self.txt_nid.get()=="" or self.txt_new_password.get()=="" or self.txt_new_cpassword.get()=="" :
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from Employees where nid=%s ",self.txt_nid.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter a valid National ID",parent=self.root)  
                elif self.txt_new_password.get()!=self.txt_new_cpassword.get():
                    messagebox.showerror("ERROR","password and confirm password do not match",parent=self.root2)         
                else:
                    cur.execute("update Employees set password=%s where nid=%s",(self.txt_new_password.get(),self.txt_nid.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","password has been reset successfuly",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)

    def forgot_password_window(self):
        if self.txt_name.get()=="":
            messagebox.showerror("Error","Please enter the name to reset your passeword",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",database="employee")
                cur=con.cursor()
                cur.execute("select * from Employees where name=%s",self.txt_name.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter a valid name to reset your passeword",parent=self.root)
                else:
                    self.root2=Toplevel()
                    self.root2.title("forgot password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")

                    t=Label(self.root2,text="forgot password",font=("time new roman",20,"bold"),bg="white",fg="green").place(x=0,y=10,relwidth=1)

                    #forgot password
                    #name label and entry
                    nid=Label(self.root2,text="National",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=90,y=100)
                    self.txt_nid=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_nid.place(x=80,y=130,width=230)
                    #new password and confirm password label and entry
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=80,y=180)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg="lightgray",show="*")
                    self.txt_new_password.place(x=80,y=200,width=230)
                    
                    new_cpassword=Label(self.root2,text="Confirm New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=80,y=250)
                    self.txt_new_cpassword=Entry(self.root2,font=("times new roman",15),bg="lightgray",show="*")
                    self.txt_new_cpassword.place(x=80,y=270,width=230)

                    chnpsw_btn = Button(self.root2,command=self.forgot_passwrord,text='Change password',fg="red",width=16,cursor="hand").place(x=120,y=330)
                con.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)



    def login_function(self):
        if self.txt_name.get()== "" or self.txt_password=="":
            messagebox.showerror("ERROR","all field are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from Employees where name=%s and password=%s",(self.txt_name.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username or password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import home_screen
                con.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)

root=Tk()
obj=login(root)
root.mainloop()
