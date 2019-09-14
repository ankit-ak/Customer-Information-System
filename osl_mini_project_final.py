from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter.messagebox as tkMessageBox
from sqlite3 import Error
from tkinter import ttk
import re



window = Tk()

database = "C:\\Users\\Ankit\\Desktop\\osl.db"  
name = ""
middle_name=""
last_name = ""
aadhar=""
reg=""
address=""
street=""
mentery = ""
eentery = ""
var = StringVar()
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
date = [int(a) for a in range(1,32)]
year = [int(a) for a in range(1900,2199)]
d=""
c=""



def Exit():
    result = tkMessageBox.askquestion('Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        window.destroy()

Top = Frame(window,width=900,height=50,bd=8,bg="black", relief="ridge")
Top.pack(side=TOP)
Left = Frame(window,width=300,height=500,relief="ridge")
Left.pack(side=LEFT)

BUTTON = Frame(Left,width=20,height=30,bg="black",relief="raise",pady=2)
BUTTON.pack(side=BOTTOM)
Right = Frame(window,width=200,height=530,bd=8,bg="black",relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left,width=650,height=350)
Forms.pack(side=TOP)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None



def create_table(conn,create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_project(conn,project):
    sql = ''' INSERT INTO data( name ,middle_name, last_name , aadhar , reg , address, street, mentery , eentery , dob)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql,project)
    return cur.lastrowid

def read():
    conn = create_connection(database)
    cursor = conn.cursor()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `data`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('','end',values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
    cursor.close()
    conn.close()


def get_data():
    name = str(s.get())
    middle_name= str(s2.get())
    last_name= str(s1.get())
    aadhar = s3.get()
    reg = s4.get()
    address = str(s5.get())
    street = str(s6.get())
    mentery = s10.get()
    eentery=s11.get()
    dob = str(date.get()+"-"+month.get()+"-"+year.get())
    print(dob)
    tkMessageBox.showinfo("Succesfull!","Information saved succesfully")
    project = [name ,middle_name, last_name , aadhar , reg , address, street, mentery , eentery , dob]
    return project

def update():
    conn = create_connection(database)
    if not tree.selection():
        print("ERROR")
    else:
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(selecteditem)
        data = get_data()
        sql = ''' UPDATE data SET
                      name = ? ,
                      middle_name= ? ,
                      last_name= ? ,
                      aadhar= ? ,
                      reg= ?,
                      address= ?,
                      street= ?,
                      mentery= ? ,
                      eentery= ?,
                      dob= ?,
                      WHERE name = ?'''
        data.append(selecteditem[0])
        print(data)
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        cur.close()
        conn.close()
        Clear()
        read()


def submit() -> object:
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS data (name TEXT PRIMARY KEY NOT NULL,
                                                                        middle_name TEXT NOT NULL,
                                                                        last_name TEXT NOT NULL, aadhar TEXT NOT NULL,
                                                                        reg TEXT NOT NULL,
                                                                        address TEXT NOT NULL, street TEXT NOT NULL, mentery TEXT NOT NULL, eentery TEXT NOT NULL, dob TEXT NOT NULL
                                                                    ); """
    conn = create_connection(database)
    cursor = conn.cursor()
    if call_me():
        data = get_data()
        if conn is not None:
        # create projects table
            create_table(conn,sql_create_projects_table)
        else:
            print("Error! cannot create the database connection.")
        with conn:
            print("Asasa")
            create_project(conn,data)

        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `data`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('','end',values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
        cursor.close()
        conn.close()
        Clear()


def update():
    conn = create_connection(database)
    if not tree.selection():
        print("ERROR")
    else:
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(selecteditem)
        data = get_data()
        sql = ''' UPDATE data SET
                      name = ? ,
                      middle_name= ? ,
                      last_name= ? ,
                      aadhar= ? ,
                      reg= ? ,   
                      address= ?,
                      street= ?,
                      mentery= ?,
                      eentery= ? ,
                      dob= ?
                      WHERE name =?'''
        data.append(selecteditem[0])
        print(data)
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        cur.close()
        conn.close()
        Clear()
        read()

def delete():
    conn = create_connection(database)
    cursor = conn.cursor()
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor.execute("DELETE FROM data WHERE name = ?",(selecteditem[0],))
            conn.commit()
            cursor.close()
            conn.close()
            Clear()
            read()

def enter(selecteditem):
    Clear()
    dob = " ".join(str(x) for x in str(selecteditem[9]).split("-"))
    dob = dob.split(" ")
    year.set(dob[2])
    month.set(dob[1])
    date.set(dob[0])
    s.set(selecteditem[0])
    s1.set(selecteditem[1])
    s2.set(selecteditem[2])
    s3.set(selecteditem[3])
    s4.set(selecteditem[4])
    s5.set(selecteditem[5])
    s6.set(selecteditem[6])
    s10.set(selecteditem[7])
    s11.set(selecteditem[8])



def Clear():
    #text.set(value=" ")
    year.set("Year")
    month.set("Month")
    date.set("Day")



def sel(a):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    enter(selecteditem)


def Exit():
    result = tkMessageBox.askquestion('Exit','Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        window.destroy()    

def call_me():
    if name.get() == '':
        messagebox.showerror('Error', 'Enter the First Name')
    elif middle_name.get() == '':
        messagebox.showerror('Error', 'Enter the Middle Name')
    elif last_name.get() == '':
        messagebox.showerror('Error', 'Enter the Last Name')
    elif (aadhar.get() == ''  or   not (aadhar.get().isdigit()) or not(len(aadhar.get())==12)):
        messagebox.showerror('Error', 'Enter the Aadhar Number')
    elif reg.get() == '' or   not (reg.get().isdigit()) or not(len(reg.get())==5):
        messagebox.showerror('Error', 'Enter the Registration Number')
    elif address.get() == '':
        messagebox.showerror('Error', 'Enter the Address')
    elif street.get() == '':
        messagebox.showerror('Error', 'Enter the Street Name')
    elif d.get() == 'Select City':
        messagebox.showerror('Error', 'Enter the City')
    elif c.get() == 'Select State':
        messagebox.showerror('Error', 'Enter the State')
    elif ((mentery.get() == '' or   not (mentery.get().isdigit()) or not(len(mentery.get())==10))):
        messagebox.showerror('Error', 'Enter the Mobile Number')
    elif eentery.get() == '' or '@' not in eentery.get()  or  '.' not in eentery.get() :
        messagebox.showerror('Error', 'Enter the email')
    elif month.get() == 'Month' or date.get() == 'Date' or year.get() == 'Year':
        messagebox.showerror('Error', 'Enter the DOB')
    else:
        messagebox.showinfo('Success','Your response successfully submitted')
        return True
def sel(a):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    print(type(selecteditem))
    enter(selecteditem)
def reset() -> object:
    name.delete(0, 'end')
    last_name.delete(0, 'end')
    middle_name.delete(0, 'end')
    aadhar.delete(0, 'end')
    reg.delete(0, 'end')
    address.delete(0, 'end')
    street.delete(0, 'end')
    mentery.delete(0, 'end')
    eentery.delete(0, 'end')
    month.set('Month')
    date.set('date')
    year.set('Year')
    d.set('Select City')
    c.set('Select State')

window.title('Customer Information System')
title_txt = Label(Top, width=900,
                  text='Customer Information System', font=('bold', 24))
title_txt.pack()
Name_label = Label(Forms, text='Enter your name:', font=('bold', 11))
s = StringVar()
name = Entry(Forms, textvariable=s)
s.set('')
s1 = StringVar()
last_name = Entry(Forms, textvariable=s1)
s1.set('')
s2 = StringVar()
middle_name = Entry(Forms, textvariable=s2)
s2.set('')


aadhar_label = Label(Forms, text='Aadhar:', font=('bold', 11))
s3 = StringVar()
aadhar = Entry(Forms, textvariable=s3)
s3.set('')

reg_label = Label(Forms, text='Registration No.:', font=('bold', 11))
s4 = StringVar()
reg = Entry(Forms, textvariable=s4)
s4.set('')


address_label = Label(Forms, text='Address:', font=('bold', 11))
s5 = StringVar()
address = Entry(Forms, textvariable=s5)
s5.set('')


street_label = Label(Forms, text='Street name:', font=('bold', 11))
s6 = StringVar()
street = Entry(Forms, textvariable=s6)
s6.set('')


Mobile_number = Label(Forms, text='Mobile number:', font=('bold', 11))
email_id = Label(Forms, text='Email id:', font=('bold', 11))
s10 = StringVar()
s11=StringVar()
mentery = Entry(Forms, textvariable=s10)
eentery = Entry(Forms, textvariable=s11)

Name_label.place(x=7, y=10)
name.place(x=10, y=35, height=25, width=165)
middle_name.place(x=185, y=35, height=25, width=165)
last_name.place(x=360, y=35, height=25, width=165)

aadhar_label.place(x=7, y=65)
aadhar.place(x=100, y=65, height=25, width=142)

reg_label.place(x=260, y=65)
reg.place(x=380, y=65, height=25, width=142)

address_label.place(x=7, y=90)
address.place(x=10, y=115, height=25, width=512)

street_label.place(x=7, y=140)
street.place(x=10, y=165, height=25, width=165)

list1 = ['Mumbai', 'Bangalore', 'Hyderabad', 'Delhi', 'Pune', 'Nagpur']
d = StringVar()
clist = OptionMenu(Forms, d, *list1)
d.set('Select City')
clist.place(x=185, y=162, height=30, width=165)

list = ['Maharashtra', 'Karnataka', 'Goa', 'Punjab', 'Andhra prades']
c = StringVar()
dlist = OptionMenu(Forms, c, *list)
c.set('Select State')
dlist.place(x=360, y=162, height=30, width=165)

Mobile_number.place(x=10, y=190)
email_id.place(x=200, y=190)
mentery.place(x=10, y=215, height=25, width=165)
eentery.place(x=200, y=215, height=25, width=327)

dob_label = Label(Forms, text='Date of Birth:', font=('bold', 11))
dob_label.place(x=7, y=240)

list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month = StringVar()
mlist = OptionMenu(Forms, month, *list)
month.set('Month')
mlist.place(x=10, y=265, height=30, width=75)

list = [int(a) for a in range(1, 32)]
date = StringVar()
dlist = OptionMenu(Forms, date, *list)
date.set('Date')
dlist.place(x=95, y=265, height=30, width=75)

list = [int(a) for a in range(1970, 2019)]
year = StringVar()
ylist = OptionMenu(Forms, year, *list)
year.set('Year')
ylist.place(x=180, y=265, height=30, width=75)

Checkbutton(Forms, text='I allow my information to be used for future campaigns').place(x=10, y=300)







yscroll = Scrollbar(Right)
yscroll.pack(side=RIGHT,fill=Y)

xscroll = Scrollbar(Right,orient="horizontal")
xscroll.pack(side=BOTTOM,fill=X)
style = ttk.Style(Right)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure("Treeview",background="#bbc4ef",
                fieldbackground="light grey",foreground="black")
tree = ttk.Treeview(Right,selectmode="browse",height=100,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)
tree.pack(side='left')
yscroll.config(command=tree.yview)
xscroll.config(command=tree.xview)


tree["columns"] = ("First Name","Middle Name","Last Name","Aadhar Number","Registration No.","Address","Street", "Mobile Number","Email","DOB",)
tree['show'] = 'headings'
tree.heading("First Name",text="First Name",anchor=W)
tree.heading("Middle Name",text="Middle Name",anchor=W)
tree.heading("Last Name",text="Last Name",anchor=W)
tree.heading("Aadhar Number",text="Aadhar Number",anchor=W)
tree.heading("Registration No.",text="Registration No.",anchor=W)
tree.heading('Address',text="Address",anchor=W)
tree.heading('Street',text="Street",anchor=W)
tree.heading("Mobile Number",text="Mobile Number",anchor=W)
tree.heading("Email",text="Email",anchor=W)
tree.heading("DOB",text="DOB",anchor=W)
tree.column('#0',stretch=NO,minwidth=0,width=0)
tree.column('#1',stretch=NO,minwidth=0,width=120)
tree.column('#2',stretch=NO,minwidth=0,width=120)
tree.column('#3',stretch=NO,minwidth=0,width=120)
tree.column('#4',stretch=NO,minwidth=0,width=120)
tree.column('#5',stretch=NO,minwidth=0,width=120)
tree.column('#6',stretch=NO,minwidth=0,width=120)
tree.column('#7',stretch=NO,minwidth=0,width=120)
tree.column('#8',stretch=NO,minwidth=0,width=120)
tree.column('#9',stretch=NO,minwidth=0,width=120)
tree.bind('<ButtonRelease-1>', sel)
read()

b1 = Button(BUTTON, text='Submit', command=submit,bg="lightblue",width=18,height=2,border=5)
b1.grid(row= 10, column=0)
b2 = Button(BUTTON, text='Reset', command=reset,bg="lightblue",width=18,height=2,border=5)
b2.grid(row= 10,column=2)
delButton = Button(BUTTON,text="DELETE",bg="lightblue",width=18,height=2,border=5,command=delete).grid(row= 10,column=3)
updateButton = Button(BUTTON,text="UPDATE",bg="lightblue",width=18,height=2,border=5, command=update).grid(row= 10,column=1)
exitButton = Button(BUTTON,text="Exit",bg="lightblue",width=18,height=2,border=5, command=Exit).grid(row= 10,column=4)



window.geometry('900x700+50+50')
window.mainloop()
