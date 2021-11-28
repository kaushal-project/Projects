from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

# Class
class Student():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # Database Information
        self.hostName_db = "localhost"
        self.userName_db = "admin"
        self.password_db = "admin@1234"
        self.databaseName_db = "SMS_db"
    
    def Window(self):
        title = Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE).pack(side=TOP,fill=X)

    # ================Variable Define===============================
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self. Email_var = StringVar()
        self.DOB_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        

    # ================== Manage Frame =============================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title = Label(Manage_Frame,text="Manage Student",font=("times new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

    # =============================Label and Entry Field ===============================
        # Roll Number
        lbl_roll = Label(Manage_Frame,text="Roll No",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        # Name
        lbl_name = Label(Manage_Frame,text="Name",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        # Email
        lbl_email = Label(Manage_Frame,text="Email",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email = Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        # Gender
        lbl_gender = Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",12,"bold"),state="readonly")
        combo_gender["values"] = ("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        # Contact
        lbl_contact = Label(Manage_Frame,text="Contact",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        # DOB
        lbl_dob = Label(Manage_Frame,text="DOB",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob = Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        # Address
        lbl_address = Label(Manage_Frame,text="Address",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address = Text(Manage_Frame,width=30,height=4,font=("times new roman",10,"bold"))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

    # ===========================Button Frame ===================================
        # Buttons
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=510,width=420)

            # Add Button
        addBtn = Button(btn_Frame,text="Add",width=6,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
            # Update Button
        updateBtn = Button(btn_Frame,text="Update",width=6,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
            # Delete
        deleteBtn = Button(btn_Frame,text="Delete",width=6,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
            # Clear BUtton
        clearBtn = Button(btn_Frame,text="Clear",width=6,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

    # ================== Detail Frame =============================
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=850,height=560)

        # Search Bar
        lbl_search = Label(Detail_Frame,text="Search By",font=("times new roman",20,"bold"),bg="crimson",fg="white").grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",12,"bold"),state="readonly",width=8)
        combo_search["values"] = ("Roll_NO","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="")

        #Search bar Entry
        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        # Btn
        searchBtn = Button(Detail_Frame,text="Search",width=6,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)

        # Show All
        showallBtn = Button(Detail_Frame,text="Show All",width=6,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

    # ====================== Table Frame =================================
        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=780,height=480)

        # Scroll Bar
        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        # Columns Declare
        self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","DOB","Gender","Contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        # Heading (column name) In Table
        self.Student_table.heading("Roll",text="Roll No")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("Address",text="Address")

        # Show only defined Heading
        self.Student_table["show"]="headings"
        
        # Size width of columns
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=150)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Gender",width=60)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("Address",width=200)

        # 
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_student(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.DOB_var.get() == "" or self.Contact_var.get() == "":
            messagebox.showerror("Error","All Fields are required.")
        else:
            # Creating a connection
            con = pymysql.connect(host=self.hostName_db,user=self.userName_db,password=self.password_db,database=self.databaseName_db)
            # Cursor
            cur = con.cursor()
            # Query
            cur.execute("INSERT INTO student_tb values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.DOB_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.txt_address.get("1.0",END)))

            # Commit Query
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Has been Inserted.")

    # 
    def fetch_data(self):
        # Creating a connection
        con = pymysql.connect(host=self.hostName_db,user=self.userName_db,password=self.password_db,database=self.databaseName_db)
        # Cursor
        cur = con.cursor()
        # Query
        cur.execute("SELECT * FROM student_tb")
        rows = cur.fetchall()
        # 
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            
            for row in rows:
                self.Student_table.insert("",END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.DOB_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,event):
        '''
            when we click on row, al the data from row where the cursor is pointed is copied in contents
        '''
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents["values"]
        
        # print(row[0])
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.DOB_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Contact_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        # Creating a connection
        con = pymysql.connect(host=self.hostName_db,user=self.userName_db,password=self.password_db,database=self.databaseName_db)
        # Cursor
        cur = con.cursor()
        # Query
        cur.execute("UPDATE student_tb SET Name = %s,Email = %s,DOB = %s,Gender = %s,Contact = %s,Address = %s WHERE Roll_NO = %s",(self.Name_var.get(),self.Email_var.get(),self.DOB_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.txt_address.get("1.0",END),self.Roll_No_var.get()))

        # Commit Query
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete_data(self):
        # Creating a connection
        con = pymysql.connect(host=self.hostName_db,user=self.userName_db,password=self.password_db,database=self.databaseName_db)
        # Cursor
        cur = con.cursor()
        # Query
        cur.execute("DELETE FROM student_tb WHERE  ROll_NO = %s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        # Creating a connection
        con = pymysql.connect(host=self.hostName_db,user=self.userName_db,password=self.password_db,database=self.databaseName_db)
        # Cursor
        cur = con.cursor()
        # Query
        cur.execute("SELECT * FROM student_tb WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        # 
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            
            for row in rows:
                self.Student_table.insert("",END,values=row)
            con.commit()
        con.close()





root = Tk()
# Object
app = Student(root)
app.Window()
root.mainloop()