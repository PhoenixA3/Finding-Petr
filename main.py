import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('PETRWATCH')
root.geometry("1200x800")  # Resizes default window size


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/David/Pictures/PETR BACKGROUND/find_petr_camera.jpg").resize((1000, 700)))


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

global score_count
score_count = 0
score_label = tkinter.Label(root, text = "SCORE:" + str(score_count), font= ('Arial', 25))
score_label.place(x=50, y=725)


def increment_score1():
    global score_count
    global button_petr1
    # print('score incremented')
    score_count += 1
    score_label.config(text = "SCORE:" + str(score_count))
    if score_count == 3:
        print("YOU FOUND ALL THE PETRS!!!")
    button_petr1 = Button(root, height=130, width=100, command=lambda: increment_score1(), image=petr1,
                          highlightthickness=0, bd=0, state=DISABLED).place(x=60, y=473)


def increment_score2():
    global score_count
    global button_petr2
    # print('score incremented')
    score_count += 1
    score_label.config(text = "SCORE:" + str(score_count))
    if score_count == 3:
        print("YOU FOUND ALL THE PETRS!!!")
    button_petr2 = Button(root, height=105, width=75, command=lambda: increment_score1(), image=petr2,
                          highlightthickness=0, bd=0, state=DISABLED).place(x=350, y=343)


def increment_score3():
    global score_count
    global button_petr3
    # print('score incremented')
    score_count += 1
    score_label.config(text = "SCORE:" + str(score_count))
    if score_count == 3:
        print("YOU FOUND ALL THE PETRS!!!")
    button_petr3 = Button(root, height=105, width=70, command=lambda: increment_score1(), image=petr3,
                          highlightthickness=0, bd=0, state=DISABLED).place(x=855, y=290)


petr1 = ImageTk.PhotoImage(Image.open("C:/Users/David/Pictures/PETR BACKGROUND/petr1.png"))
petr2 = ImageTk.PhotoImage(Image.open("C:/Users/David/Pictures/PETR BACKGROUND/petr2.png"))
petr3 = ImageTk.PhotoImage(Image.open("C:/Users/David/Pictures/PETR BACKGROUND/petr3.png"))


button_petr1 = Button(root, height=130, width=100, command=lambda:increment_score1(), image = petr1, highlightthickness = 0, bd = 0).place(x=60, y=473)
# make_invisible(button_petr1)

button_petr2 = Button(root, height=105, width=75, command=lambda:increment_score2(), image = petr2, highlightthickness = 0, bd = 0).place(x=350, y=343)

button_petr3 = Button(root, height=105, width=70, command=lambda:increment_score3(), image = petr3, highlightthickness = 0, bd = 0).place(x=855, y=290)

# make a label displays score

root.mainloop()
