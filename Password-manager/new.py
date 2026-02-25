from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
    special_character = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                         '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

    value1 = [choice(number_list) for _ in range(randint(8, 10))]
    value2 = [choice(letter_list) for _ in range(randint(2, 4))]
    value3 = [choice(special_character) for _ in range(randint(2, 4))]
    new_password = value1 + value2 + value3
    shuffle(new_password)

    password = "".join(new_password)
    third.insert(0,password)
    if third.get =="":
        third.insert(END, string=f"{password}")
    else:
        third.delete(0,END)
        third.insert(END, string=f"{password}")

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def create():
    data1=first.get()
    data2=second.get()
    data3=third.get()
    new_data={data1:{
        "email":data2,
        "password":data3,
    }}

    if len(data1)==0 or len(data2)==0 or len(data3) == 0:
        messagebox.showerror(title="oops", message="you have not entered the values")
        print("invalid inputs")
    else:
        try:
            with open("data.json", "r") as data_file:
            # READING THE DATA
                data = json.load(data_file)
            # WRITING IN DATA
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                 json.dump(new_data,data_file,indent=4)
        else:
            # UPDATING THE DATA
            data.update(new_data)
            with open("data.json", "w") as data_file:
                 json.dump(data,data_file,indent=4)
            # print(data)
        finally:
            first.delete(0,END)
            third.delete(0,END)

# ---------------------------- Search ------------------------------- #
def search():
    value1=first.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message="FILE NOT FOUND")
    else:
         if value1 in data:
             email=data[value1]["email"]
             value=data[value1]["password"]
             messagebox.showinfo(title=value1, message=f"email:{email}\n password:{value}")
         else :
             messagebox.showinfo(title="oops", message="VALUE NOT FOUND")


# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.config(bg=YELLOW)
windows.title("THE PASSSWORD MANAGER")
windows.config(padx=50,pady=50)


canvas=Canvas(height=200,width=200,bg=YELLOW,highlightthickness=0)
my_image=PhotoImage(file="logo.png")
canvas.configure()
canvas.create_image(100,100,image=my_image)
canvas.grid(row=0,column=1,)

# LABELS
label1 = Label(text="WEBSITE:",bg=YELLOW,highlightthickness=0)
label1.grid(row=1,column=0)

label2=Label(text="EMAIL/USERNAME:",bg=YELLOW,highlightthickness=0)
label2.grid(row=2,column=0)

label3=Label(text="Password:",bg=YELLOW,highlightthickness=0)
label3.grid(row=3,column=0)

# ENTRIES
first=Entry(width=34)
first.focus()
first.grid(row=1,column=1)

second=Entry(width=57)
second.insert(END,string="suraj1208@gmail.com")
second.grid(row=2,column=1,columnspan=2)

third=Entry(width=34)
third.insert(END,string="")
third.grid(row=3,column=1)

# BUTTONS
button1=Button(text="GENERATE PASSWORD",command=generate)
button1.grid(column=2,row=3)

button2=Button(text="ADD PASSWORD",width=49,command=create)
button2.grid(row=4,column=1,columnspan=2)

button3=Button(text="SEARCH",width=18,command=search)
button3.grid(row=1,column=2)



windows.mainloop()