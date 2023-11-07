from tkinter import *
from random import *
window = Tk()
window.title('Dice simulator')
canvas = Canvas(window, width=800, height=500, bg='brown')
canvas.pack()
dice = canvas.create_rectangle(375, 225, 425, 275, fill='white')
rollnum2 = canvas.create_text(400, 250, text=str(randint(1, 6)), font=50)



