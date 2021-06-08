# ============================imports========================
from tkinter import *
from tkinter import messagebox, filedialog, OptionMenu, ttk
from datetime import datetime
from sqlite3 import connect
import os
from PIL import Image
from PIL import ImageFilter
import re

# ============================ StartUp Page==================
root = Tk()


def action1():
    root.geometry("700x310")
    # root.resizable(0, 0)
    root.title("School")
    def all_children(root):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()
        item.place_forget()
        item.pack_forget()

    store = StringVar()
    store2 = StringVar()
    store3 = IntVar()
    store4 = StringVar()
    store5 = Variable()
    store6 = StringVar()
    store7 = StringVar()
    store8 = IntVar()
    store9 = StringVar()
    List1 = list()
    List2 = [
        'Male',
        'Female'
    ]
    List3 = ['Abia', 'Adamawa', 'Akwa-Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 
    'Cross-River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna',
    'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun',
    'Oyo', 'Plateau', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara', 'F.C.T Abuja']
    options = range(1990, datetime.now().year + 1)
    for i in options:
        List1.append(i)
    store3.set(List1[0])
    store4.set(List2[0])
    store8.set(List1[0])
    store6.set('Choose state')
    store5.set('dd/mm/yy')
    
                                            #   Functions
    def check():
        lname = store.get()
        fname = store2.get()
        admin_yr = store3.get()
        gender = store4.get()
        dob = store5.get()
        state = store6.get()
        admin_no = store7.get()
        grad_yr = store8.get()
        others = docs_entry.get()

        if lname.strip() != '' and fname.strip() != '' and gender.strip() != '' and state.strip() != '' and admin_no.strip() != '' and others.strip() != '':
            day, month, year = dob.split('/')
            isValidDate = True
            try:
                datetime(int(year), int(month), int(day))
            except ValueError:
                isValidDate = False
            if not isValidDate:
                messagebox.showinfo('Incorrect Date', 'Please enter a valid date')
            elif int(grad_yr) == int(admin_yr):
                messagebox.showinfo('Error', 'Invalid Graduation Year')                
            elif int(grad_yr) < int(admin_yr):
                messagebox.showinfo('Error', 'Graduation year cannot be before Admission year')
            elif state == 'Choose state':
                messagebox.showinfo('Error', 'Enter a valid state')
            if re.findall(r'[a-zA-Z]+', lname) and re.findall(r'[a-zA-Z ]+', fname):
                if re.findall(r'[0-9a-zA-z]+', admin_no):
                    process()
                else:
                    messagebox.showinfo('Error', 'Enter valid Admission Number')
            else:
                messagebox.showinfo('Error', 'Enter a valid name')
        else:
            messagebox.showinfo('Error', 'All fields are compulsory')


    def process():
        lname = store.get().capitalize()
        fname = store2.get().capitalize()
        admin_yr = store3.get()
        gender = store4.get().capitalize()
        dob = store5.get()
        state = store6.get()
        admin_no = store7.get()
        grad_yr = store8.get()
        others = docs_entry.get()

        conn = connect('Schooldatabase.db')
        create = conn.cursor()
        create.execute('''CREATE TABLE IF NOT EXISTS Students
        (
            FULLNAME varchar(40),
            AdminNO nvarchar(8),
            DOB datetime,
            Gender varchar(10),
            State varchar(15),
            AdminYr nvarchar(4),
            GradYr nvarchar(4)
        )''',
                    )
        create.execute('Insert into Students values(?,?,?,?,?,?,?)',
                    (lname + ' ' + fname, admin_no, dob, gender, state, admin_yr, grad_yr))
        conn.commit()

        name = lname + ' ' + fname
        root_directory = os.getcwd()
        path1 = os.path.join(root_directory, 'SchoolDatabase',  str(admin_yr))
        path2 = os.path.join(path1, name)
        os.chdir(root_directory)
        os.makedirs(path2)
        
        inPath = others
        outPath = path2

        for imagepath in os.listdir(inPath):
            if imagepath.endswith('.jpg'):
                inputPath = os.path.join(inPath, imagepath)
                img = Image.open(inputPath)
                fullOutPath = os.path.join(outPath, 'invert_' + imagepath)
                img.save(fullOutPath)

        messagebox.showinfo('Successful', 'Database Created successfully')
        root.destroy()


    def check_file():
        file = filedialog.askdirectory()
        store9.set(file)


    #                                               widgets
    heading = Label(root, text="STUDENTS RECORD BOOK", font=" , 25")
    last_name = Label(root, text="Last Name", font=" , 13")
    last_name_entry = Entry(root, borderwidth=6, justify='center', font=' , 13', textvariable=store)
    others = Label(root, text="Other Names", font=" , 13")
    others_entry = Entry(root, borderwidth=6, justify='center', font=' , 13', textvariable=store2)
    admin_year = Label(root, text="Admin. Year", font=' , 13')
    admin_year_entry = OptionMenu(root, store3, *List1)
    grad_year = Label(root, text="Grad. Year", font=' , 13')
    grad_year_entry = OptionMenu(root, store8, *List1)
    gender_lab = Label(root, text='Gender', font=' , 13')
    gender_entry = OptionMenu(root, store4, *List2)
    dob_lab = Label(root, text='D.O.B', font=' , 13')
    dob_entry = Entry(root, textvariable=store5, borderwidth=2, justify='left', font=' , 11')
    state_lab = Label(root, text='State of Origin', font=' , 13')
    state_entry = OptionMenu(root, store6, *List3)
    admin = Label(root, text='Admin NO.', font=' , 13')
    admin_entry = Entry(root, textvariable=store7, borderwidth=2, justify='left', font=' , 11')
    docs = Label(root, text='Related Documents', font=' , 13')
    docs_entry = Entry(root, borderwidth=5, justify='left', font=' , 11', textvariable=store9)
    search = Button(root, text='Browse', font=' , 10', command=check_file)
    last = Button(root, text='Save', borderwidth=2, font=' , 13', command=check)
    exit_button = Button(root, text='Back', borderwidth=2, font=' , 13', command=lambda: start())

    heading.place(x=123)
    last_name.place(y=140)
    last_name_entry.place(x=85, y=135)
    others.place(y=140, x=330)
    others_entry.config(width=25)
    others_entry.place(y=135, x=433)
    admin_year.place(y=90)
    admin_year_entry.place(y=85, x=100)
    admin.place(y=90, x=250)
    admin_entry.config(width=8)
    admin_entry.place(y=85, x=340)
    grad_year.place(y=90, x=490)
    grad_year_entry.place(y=85, x=580)
    dob_lab.place(y=190)
    dob_entry.config(width=10)
    dob_entry.place(y=190, x=57)
    state_lab.place(y=190, x=200)
    state_entry.place(y=185, x=310)
    gender_lab.place(y=190, x=480)
    gender_entry.place(y=185, x=540)
    docs.place(y=240)
    docs_entry.config(width=50)
    docs_entry.place(y=235, x=150)
    search.config(width=8)
    search.place(y=235, x=560)
    last.configure(width=6)
    last.place(x=280, y=270)
    exit_button.configure(width=6)
    exit_button.place(x=400, y=270)


def action2():
    root.title("Students Data")
    root.geometry('')
    def all_children(root):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()
        item.place_forget()
        item.pack_forget()

    List = []
    def check_file(text):

        root.geometry('700x600')

        def all_children(root):
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())
            return _list

        widget_list = all_children(root)
        for item in widget_list:
            item.grid_forget()
            item.place_forget()
            item.pack_forget()
        conn = connect('Schooldatabase.db')
        create = conn.cursor()
        z = create.execute("Select * from Students where GradYr = " + text + " order by FULLNAME asc")
        rows = z.fetchall()
        conn.commit()
        heading = text + ' Students'
        title = Label(root, text=heading, font=' , 20')
        back_button = Button(root, width=6, text='Back', font=' , 15', command=lambda: action2())

        tv = ttk.Treeview(root, show='headings', selectmode='browse', height=25)
        tv.pack(side=LEFT)
        tv.place(x=0, y=38)

        tv['columns'] = ('Fullname', 'Admin_no', 'D.O.B', 'Gender', 'State', 'Admin_yr', 'Grad_yr')
        tv.column('Fullname', anchor=W, width=150)
        tv.column('Admin_no', anchor=CENTER, width=90)
        tv.column('D.O.B', anchor=CENTER, width=90)
        tv.column('Gender', anchor=CENTER, width=90)
        tv.column('State', anchor=CENTER, width=90)
        tv.column('Admin_yr', anchor=CENTER, width=90)
        tv.column('Grad_yr', anchor=CENTER, width=90)

        # tv.heading('SN', text='SN', anchor=W)
        tv.heading('Fullname', text='FULLNAME', anchor=CENTER)
        tv.heading('Admin_no', text='ADMIN_NO', anchor=CENTER)
        tv.heading('D.O.B', text='DOB', anchor=CENTER)
        tv.heading('Gender', text='GENDER', anchor=CENTER)
        tv.heading('State', text='STATE', anchor=CENTER)
        tv.heading('Admin_yr', text='ADMIN_YR', anchor=CENTER)
        tv.heading('Grad_yr', text='GRAD_YR', anchor=CENTER)

        title.pack(side=TOP)
        for i in rows:
            tv.insert('', 'end', values=i)
        
        yscrollbar = ttk.Scrollbar(root, orient='vertical', command=tv.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        tv.configure(yscrollcommand=yscrollbar.set)
        back_button.pack(side=BOTTOM)

    conn = connect('Schooldatabase.db')
    create = conn.cursor()
    create.execute('''CREATE TABLE IF NOT EXISTS Students
        (
            FULLNAME varchar(40),
            AdminNO nvarchar(8),
            DOB datetime,
            Gender varchar(10),
            State varchar(15),
            AdminYr nvarchar(4),
            GradYr nvarchar(4)
        )''',
                    )
    create.execute("Select GradYr from Students")
    z = create.fetchall()
    conn.commit()
    times = 0
    change = tuple(z)
    while times < len(change):
        for item in z[times]:
            List.append(item)
        times += 1

    new_list = []

    for i in set(List):
        new_list.append(i)

    sorted_list = sorted(new_list)

    sort_1 = sorted_list[0: 6]
    sort_2 = sorted_list[6: 12]
    sort_3 = sorted_list[12: 18]
    sort_4 = sorted_list[18: 24]
    sort_5 = sorted_list[24: 30]
    sort_6 = sorted_list[30: 36]
    sort_7 = sorted_list[36: 42]
    sort_8 = sorted_list[42: 48]
    sort_9 = sorted_list[48: 54]
    sort_10 = sorted_list[54: 60]
    buttonRows = ["SELECT STUDENT'S GRADUATION YEAR", sort_1, sort_2, sort_3, sort_4, sort_5, sort_6,
    sort_7, sort_8, sort_9, sort_10, 'Back']

    title = Label(root, text=buttonRows[0], font=' , 20')
    exit_button = Button(root, text=buttonRows[-1], borderwidth=2, font=' , 13', command=lambda: start())
    
    title.grid(row=0, column=1, columnspan=4)
    exit_button.configure(width=6)
    exit_button.grid(row=buttonRows.index(buttonRows[-1]), column=2, columnspan=2)
    
    for row_index, row in enumerate(buttonRows[1:-1]):
        for cell_index, cell in enumerate(row):
            btns = Button(root, text=cell, font=' , 13', command= lambda text=cell: check_file(text))
            btns.configure(width=9, relief=RIDGE)
            btns.grid(row=row_index+1, column=cell_index, padx=3, pady=3)
    # else:
    #     root.geometry('500x300')
    #     err_label = Label(
    #         root,
    #         text="There's no data to display",
    #         font=' , 15'
    #     )
    #     err_button = Button(
    #         root,
    #         text='Back',
    #         borderwidth=5,
    #         font=' , 13',
    #         command=lambda : start()
    #     )
    #     err_label.pack()
    #     err_button.pack()
    


def start():
    
    def all_children(root):
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())
            return _list

    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()
        item.place_forget()
        item.pack_forget()
    root.geometry("700x310")
    # root.resizable(0, 0)
    root.title("School")


    def destroy():
        root.destroy()
    

    button1 = Button(root, text="Add new Student's Record", font=', 18', command=action1)
    button2 = Button(root, text="Browse Students Records", font=', 18', command=action2)
    exit_button = Button(root, text='Exit', font=' , 15', command=destroy)

    button1.configure(relief=SUNKEN)
    button1.place(y=80, x=20)
    button2.configure(relief=SUNKEN)
    button2.place(y=80, x=360)
    exit_button.configure(width=10)
    exit_button.place(y=220, x=280)


if __name__ == '__main__':
    start()
    
root.mainloop()
