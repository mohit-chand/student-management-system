import tkinter as tk
import file_2 as sq

mainWindow=tk.Tk()
mainWindow.title(" STUDENT MANAGEMENT SYSTEM")

label=tk.Label(mainWindow,text=" Enter name ",)
label.pack()

name_field_1=tk.Entry(mainWindow)
name_field_1.pack()

label=tk.Label(mainWindow,text="enter college name ",)
label.pack()

college_field_1=tk.Entry(mainWindow)
college_field_1.pack()

label=tk.Label(mainWindow,text="enter address",)
label.pack()

address_field_1=tk.Entry(mainWindow)
address_field_1.pack()

label=tk.Label(mainWindow,text="enter phone number",)
label.pack()

phone_field_1=tk.Entry(mainWindow)
phone_field_1.pack()

label=tk.Label(mainWindow,text="enter entry to delete")
label.pack()

delete_field=tk.Entry(mainWindow)
delete_field.pack()

create_button=tk.Button(mainWindow,text=" Create Table ",command=lambda: createtable())
create_button.pack()

insert_button=tk.Button(mainWindow,text=" Insert Table",command=lambda: insertvalues())
insert_button.pack()

retrieve_button=tk.Button(mainWindow,text=" Retrieve Table",command=lambda: retrievevalues())
retrieve_button.pack()

delete_button=tk.Button(mainWindow,text=" Delete Entry",command=lambda: deletevalues())
delete_button.pack()

def createtable():
    print("table created successfully")
    sq.create_table()

def insertvalues():
    name=name_field_1.get()
    college=college_field_1.get()
    address=address_field_1.get()
    phone=phone_field_1.get()

    sq.insert_table(name,college,address,phone)

def retrievevalues():
    print("data retrieved successfully")
    sq.retrieve_data()

def deletevalues():
    id=delete_field.get()
    print("entry deleted successfully")
    sq.delete_data(id)

mainWindow.mainloop()