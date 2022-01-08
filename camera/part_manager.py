from tkinter import *
from tkinter import messagebox
from db import Database
db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if name_text.get() == '' or phone_text.get() == '' or address_text.get() == '' or nid_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(name_text.get(), phone_text.get(), address_text.get(), nid_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (name_text.get(), phone_text.get(), address_text.get(), nid_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        phone_entry.delete(0, END)
        phone_entry.insert(END, selected_item[2])
        address_entry.delete(0, END)
        address_entry.insert(END, selected_item[3])
        nid_entry.delete(0, END)
        nid_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], name_text.get(), phone_text.get(), address_text.get(), nid_text.get())
    populate_list()


def clear_text():
    name_entry.delete(0, END)
   
    phone_entry.delete(0, END)

    address_entry.delete(0, END)
 
    nid_entry.delete(0, END)


# create a window
app = Tk()
# part 1 name
name_text = StringVar()
name_label = Label(app, text='Employee Name', font=('bold', 9), pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(app, textvariable=name_text)
name_entry.grid(row=0, column=1)

# part 2 phone
phone_text = StringVar()
phone_label = Label(app, text='Phone number', font=('bold', 9))
phone_label.grid(row=0, column=2, sticky=W)
phone_entry = Entry(app, textvariable=phone_text)
phone_entry.grid(row=0, column=3)

# part 3 address
address_text = StringVar()
address_label = Label(app, text='Address', font=('bold', 9))
address_label.grid(row=1, column=0, sticky=W)
address_entry = Entry(app, textvariable=address_text)
address_entry.grid(row=1, column=1)

# part 4 national ID
nid_text = StringVar()
nid_label = Label(app, text='National ID', font=('bold', 9))
nid_label.grid(row=1, column=2, sticky=W)
nid_entry = Entry(app, textvariable=nid_text)
nid_entry.grid(row=1, column=3)

# part list (listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# buttons 1
add_btn = Button(app, text='add part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)
# buttons 2
remove_btn = Button(app, text='remove part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)
# buttons 3
update_btn = Button(app, text='update part', width=12, command=update_item)
update_btn.grid(row=2, column=2)
# buttons 4
clear_btn = Button(app, text='clear part', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app.title('Add employees')
app.geometry('700x400')


# start program
app.mainloop()
