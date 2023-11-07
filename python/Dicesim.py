from tkinter import *
from random import *
def roll():
    txt.delete(0.0, END)
    txt.insert(END, str(randint(1,6)))
window = Tk()
window.title('Dice simulator')
canvas = Canvas(window, width=800, height=500, bg='brown')
canvas.pack()
dice = canvas.create_rectangle(375, 225, 425, 275, fill='white')
frame = Frame(canvas, width=25, height=15)
window = canvas.create_window(400, 295, window=frame)
txtframe = Frame(canvas, width=50, height=50)
txtwindow = canvas.create_window(400, 250, window=txtframe, width=49, height=49)
txt = Text(txtframe, font=50)
button = Button(frame, text='Roll', command=roll)
button.pack()
txt.pack()




