from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from db import Database
import pymysql
import re
import tkinter as tk
class regemp:
    def __init__(self,root):
        self.root=root
        self.root.title("PANOPTES")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)
        #register emplyees frame#
        # frame1=Frame(self.root,bg="white")
        # frame1.place(x=350,y=50,width=600,height=500)
        title=Label(self.root,text="Register Employees",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="chocolate2",fg="white").place(x=550,y=0)
        backbtn=Button(self.root,text="BACK",command=self.home_screen,cursor="hand",fg='Red',width=9).place(x=50,y=660)
        logout=Button(self.root,text="Log Out",command=self.logout,cursor="hand",fg='Red',width=9).place(x=1250,y=660)
        #logo
        root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='panoptes.png'))

        #variables
        self.name_var=StringVar()
        self.phone_var=StringVar()
        self.address_var=StringVar()
        self.nid_var=StringVar()
        self.age_var=StringVar()
        self.gender_var=StringVar()
        self.position_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


        #manage frame
        manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=70,width=450,height=560)
        m_title=Label(manage_frame,text="Add employees",bg="chocolate2",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,padx=100,pady=20)
       

        #emplyee details
        #employee name
        name=Label(manage_frame,fg="black",text="Name",font=("times new roman",20,"bold"))
        name.grid(row=1,column=0,padx=20,pady=10,sticky=W)

        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=10,padx=20,sticky=W)

        #employee phone
        phone=Label(manage_frame,fg="black",text="Phone",font=("times new roman",20,"bold"))
        phone.grid(row=2,column=0,padx=20,pady=10,sticky=W)

        txt_phone=Entry(manage_frame,textvariable=self.phone_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_phone.grid(row=2,column=1,pady=10,padx=20,sticky=W)

        #employee address
        address=Label(manage_frame,fg="black",text="Address",font=("times new roman",20,"bold"))
        address.grid(row=3,column=0,padx=20,pady=10,sticky=W)

        txt_address=Entry(manage_frame,textvariable=self.address_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_address.grid(row=3,column=1,pady=10,padx=20,sticky=W)

        # self.txt_address=Text(manage_frame,width=30,height=4,font=("",10))
        # self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="W")
        #employee national id
        nid=Label(manage_frame,fg="black",text="National ID",font=("times new roman",20,"bold"))
        nid.grid(row=4,column=0,padx=20,pady=10,sticky=W)

        txt_nid=Entry(manage_frame,textvariable=self.nid_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_nid.grid(row=4,column=1,pady=10,padx=20,sticky=W)

        #employee age
        age=Label(manage_frame,fg="black",text="Age",font=("times new roman",20,"bold"))
        age.grid(row=5,column=0,padx=20,pady=10,sticky=W)

        txt_age=Entry(manage_frame,textvariable=self.age_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        txt_age.grid(row=5,column=1,pady=10,padx=20,sticky=W)

        #employee gender
        gender=Label(manage_frame,fg="black",text="Gender",font=("times new roman",18,"bold"))
        gender.grid(row=6,column=0,padx=20,pady=10,sticky=W)

        txt_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new roman",18,"bold"),state='readonly')
        txt_gender['values']=("Select","Female","Male",)
        txt_gender.grid(row=6,column=1,pady=10,padx=20,sticky=W)
        txt_gender.current(0)
        
        #employee position
        position=Label(manage_frame,fg="black",text="Position",font=("times new roman",18,"bold"))
        position.grid(row=7,column=0,padx=20,pady=10,sticky=W)

        txt_position=ttk.Combobox(manage_frame,textvariable=self.position_var,font=("times new roman",18,"bold"),state='readonly')
        txt_position['values']=("Select","Owner","Employee","Security",)
        txt_position.grid(row=7,column=1,pady=10,padx=20,sticky=W)
        txt_position.current(0)



        #btn manage frame add remove updat clear
        btn_frame=Frame(manage_frame,cursor="hand",bd=4,relief=RIDGE,bg="chocolate2")
        btn_frame.place(x=5,y=500,width=430)

        addbtn=Button(btn_frame,text="ADD",width=9,command=self.add_employee).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="UPDATE",width=9,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="DELETE",width=9,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="CLEAR",width=9,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #detail frame
        detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        detail_frame.place(x=500,y=70,width=800,height=560)


        search=Label(detail_frame,text="Search by",font=("times new roman",18,"bold"))
        search.grid(row=0,column=0,pady=10,padx=20,sticky="W")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("Name","Position","Age")
        combo_search.grid(row=0,column=1,padx=20,pady=20)

        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        search_btn=Button(detail_frame,cursor="hand",text="Search",width=10,fg="chocolate2",command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(detail_frame,cursor="hand",text="Show All",width=10,fg="chocolate2",command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #results frame
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE)
        table_frame.place(x=10,y=70,width=760,height=475)

        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        self.employee_table=ttk.Treeview(table_frame,columns=("Name","Phone","Address","National_ID","Age","Gender","Position"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,show='headings')

        scroll_x.pack(side=BOTTOM,fill=X)        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview) 
        scroll_y.config(command=self.employee_table.yview) 

        self.employee_table.heading("Name",text="Names")
        self.employee_table.heading("Phone",text="Phone")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("National_ID",text="National ID")
        self.employee_table.heading("Age",text="Age")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("Position",text="Position")

        self.employee_table.column("Name",width=120)
        self.employee_table.column("Phone",width=120)
        self.employee_table.column("Address",width=120)
        self.employee_table.column("National_ID",width=120)
        self.employee_table.column("Age",width=120)
        self.employee_table.column("Gender",width=120)
        self.employee_table.column("Position",width=120)
        self.employee_table['show']='headings'
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def special_match(self,strg, search=re.compile(r'[^a-zA-Z.]').search):
        return not bool(search(strg))

    def num_match(self,strg, search=re.compile(r'[^0-9.]').search):
        return not bool(search(strg))

    def add_employee(self):
        if self.name_var.get()=="" or self.phone_var.get()=="" or self.address_var.get()=="" or self.nid_var.get()=="" or self.age_var.get()=="" or self.gender_var.get()=="" or self.position_var.get()=="select" :
            messagebox.showerror("ERROR","all field are required")
        elif self.special_match(self.name_var.get())==False :
            messagebox.showerror("Error!", "Name should only have Characters")
        elif len(self.phone_var.get())<11 or self.num_match(self.phone_var.get())==False   :
            messagebox.showerror("Error!", "Mobile should contain only numbers and should be 11 numbers ")
        elif len(self.nid_var.get())<14 or self.num_match(self.nid_var.get())==False   :
            messagebox.showerror("Error!", "National ID should contain only numbers and should be 14 numbers ")
        elif self.num_match(self.age_var.get())==False  :
            messagebox.showerror("Error!", "Age should contain only numbers ")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="employee")
            cur=con.cursor()
            cur.execute("select * from emp where National_ID=%s",self.nid_var.get())
            row=cur.fetchone() 
            #  print(row)
            if row!=None:
                messagebox.showerror("Error","Employee already exists",parent=self.root)
            else:
                cur.execute("insert into emp values(%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                            self.phone_var.get(),
                                                                            self.address_var.get(),
                                                                            self.nid_var.get(),
                                                                            self.age_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.position_var.get()
                                                                            ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Employee registered successfuly")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("select * from emp")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        self.nid_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.position_var.set("")

    def get_cursor(self,ev):
        curosor_row=self.employee_table.focus()
        contents=self.employee_table.item(curosor_row)
        row=contents['values']
        self.name_var.set(row[0])
        self.phone_var.set(row[1])
        self.address_var.set(row[2])
        self.nid_var.set(row[3])
        self.age_var.set(row[4])
        self.gender_var.set(row[5])
        self.position_var.set(row[6])
    
    def update_data(self):
        
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("update emp set Name=%s,Phone=%s,Address=%s,Age=%s,Gender=%s,Position=%s where National_ID=%s",(
                                                                    self.name_var.get(),
                                                                    self.phone_var.get(),
                                                                    self.address_var.get(),
                                                                    self.age_var.get(),
                                                                    self.gender_var.get(),
                                                                    self.position_var.get(),
                                                                    self.nid_var.get()
                                                                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("delete from emp where National_ID=%s", self.nid_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("select * from emp where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def home_screen(self):
        self.root.destroy()
        import home_screen
    def logout(self):
        self.root.destroy()
        import login_screen

root=Tk()
obj=regemp(root)
root.mainloop()
