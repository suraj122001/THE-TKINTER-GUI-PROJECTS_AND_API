from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

try:
    file_csv = pandas.read_csv("./data/values_to_learn.csv")
except FileNotFoundError:
    original_csv = pandas.read_csv("./data/french_words.csv")
    values = original_csv.to_dict(orient="records")
else:
    values = file_csv.to_dict(orient="records")




def next_card():
    global current_card,flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(values)
    canvas.itemconfig(text1, text="French",fill="black")
    canvas.itemconfig(text2,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=image2)
    flip_timer=windows.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=image1)
    canvas.itemconfig(text1,text="English",fill="white")
    canvas.itemconfig(text2, text=current_card["English"],fill="white")

def known_card():
    values.remove(current_card)
    new=pandas.DataFrame(values)
    new.to_csv("./data/values_to_learn.csv",index=False)
    next_card()


windows=Tk()
windows.title("flash")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=windows.after(3000,func=flip_card)




canvas=Canvas(width=800,height=526)

image1=PhotoImage(file="images/card_back.png")
image2=PhotoImage(file="images/card_front.png")
image3=PhotoImage(file="images/right.png")
image4=PhotoImage(file="images/wrong.png")

canvas_image=canvas.create_image(400,263,image=image2)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
text1=canvas.create_text(400,150,text="",fill="black",font=("Courier",35,"italic"))
text2=canvas.create_text(400,300,text="",fill="black",font=("Courier",60,"bold"))



tick_button=Button(height=100,width=100,image=image3,command=known_card,highlightthickness=0)
tick_button.grid(row=1,column=0)

wrong_button=Button(height=100,width=100,image=image4,command=next_card,highlightthickness=0)
wrong_button.grid(row=1,column=1)


next_card()


# pandas.DataFrame(file)
# value_dict={French:English for (French,English) in file.iterrows()}
# check=value_dict[English]
# birthday_dict={data_row.French:data_row.English for (index,data_row) in file.iterrows()}
# print(birthday_dict.keys())
# print(check)














windows.mainloop()