from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEXT="✔"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 25
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    windows.after_cancel(timer)
    my_label.config(text="THE POMODARA TIMER", font=("Arial", 20), width=20, fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    tick.config(font=("Arial", 20), width=20, fg=GREEN, bg=YELLOW)
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    work_sec=WORK_MIN * 60
    short_break=SHORT_BREAK_MIN * 60
    long_break=LONG_BREAK_MIN*60

    reps+=1
    print(reps)
    if reps % 2==0:
        count_down(short_break)
        my_label.config(text="BREAK TIME",fg=PINK)

    elif reps % 8==0:
        count_down(long_break)
        my_label.config(text="BREAK TIME",fg=RED)
        # my_label = Label(text="BREAK TIME", font=("Arial", 20), width=20, fg=RED, bg=YELLOW)
        # my_label.grid(column=2, row=1)
    else:
        count_down(work_sec)
        my_label.config(text="WORK TIME", fg=GREEN)
        # my_label = Label(text="WORK TIME", font=("Arial", 20), width=20, fg=GREEN, bg=YELLOW)
        # my_label.grid(column=2, row=1)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def increase_tick():
#     column=0
#     tick1 = Label(text=TEXT, font=("Arial", 20), width=20, fg=GREEN, bg=YELLOW)
#     tick1.grid(column=2, row=5)
#     pass
def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count % 60
    # if count_sec == 0:
    #     count_sec="00"
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000,count_down,count-1)
    else:
        timer_start()
        sign=" "
        work_session=math.floor(reps / 2)
        for _ in range(work_session):
           sign+=TEXT
           tick.config(text=sign, fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
# windows.minsize(width=600,height=400)
windows.configure(bg="white")
windows.title("THE PAMODARO TECHNIQUE")
windows.config(padx=100,pady=50,bg=YELLOW)


my_label=Label(text="THE POMODARA TIMER",font=("Arial",20),width=20,fg=GREEN,bg=YELLOW)
# my_label.pack()
my_label.grid(column=2,row=1)


canvas=Canvas(width=204,height=228,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(102,114,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
# canvas.pack()
canvas.grid(column=2,row=3)



tick=Label(font=("Arial",20),width=20,fg=GREEN,bg=YELLOW)
# tick.pack()
tick.grid(column=2,row=5)


start=Button(text="Start",command=timer_start,highlightthickness=0)
# start.pack(side="right")
start.grid(column=1,row=5)


reset=Button(text="reset",command=timer_reset,highlightthickness=0)
# stop.pack(side="left")
reset.grid(column=3,row=5)







windows.mainloop()