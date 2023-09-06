from tkinter import *

window = Tk()
window.title("Calculator")

# Data Entry
e_text = Entry(window, font= ("Calibri 20"))
e_text.grid(row= 0, column= 0, columnspan= 4, padx= 50, pady= 5)

# Buttons
button1 = Button(window, text= "1", width= 5, height= 2)
button2 = Button(window, text= "2", width= 5, height= 2)
button3 = Button(window, text= "3", width= 5, height= 2)
button4 = Button(window, text= "4", width= 5, height= 2)
button5 = Button(window, text= "5", width= 5, height= 2)
button6 = Button(window, text= "6", width= 5, height= 2)
button7 = Button(window, text= "7", width= 5, height= 2)
button8 = Button(window, text= "8", width= 5, height= 2)
button9 = Button(window, text= "9", width= 5, height= 2)
button0 = Button(window, text= "0", width= 13, height= 2)

button_delete = Button(window, text= "AC", width= 5, height= 2)
button_left_parenthesis = Button(window, text= "", width= 5, height= 2)
button_right_parenthesis = Button(window, text= "", width= 5, height= 2)
button_period = Button(window, text= "", width= 5, height= 2)

button_div = Button(window, text= "/", width= 5, height= 2)
button_mult = Button(window, text= "x", width= 5, height= 2)
button_plus = Button(window, text= "+", width= 5, height= 2)
button_subtraction = Button(window, text= "-", width= 5, height= 2)
button_result = Button(window, text= "=", width= 5, height= 2)


window.mainloop()