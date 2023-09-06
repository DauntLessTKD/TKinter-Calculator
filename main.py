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
button0 = Button(window, text= "0", width= 19, height= 2)

button_delete = Button(window, text= "AC", width= 5, height= 2)
button_left_parenthesis = Button(window, text= "(", width= 5, height= 2)
button_right_parenthesis = Button(window, text= ")", width= 5, height= 2)
button_period = Button(window, text= "", width= 5, height= 2)

button_div = Button(window, text= "/", width= 5, height= 2)
button_mult = Button(window, text= "x", width= 5, height= 2)
button_plus = Button(window, text= "+", width= 5, height= 2)
button_subtraction = Button(window, text= "-", width= 5, height= 2)
button_result = Button(window, text= "=", width= 5, height= 2)

# Add the buttons to the window
button_delete.grid(row= 1, column= 0, padx= 5, pady= 5)
button_left_parenthesis.grid(row= 1, column= 1, padx= 5, pady= 5)
button_right_parenthesis.grid(row= 1, column= 2, padx= 5, pady= 5)
button_div.grid(row= 1, column= 3, padx= 5, pady= 5)

button7.grid(row= 2, column= 0, padx= 5, pady= 5)
button8.grid(row= 2, column= 1, padx= 5, pady= 5)
button9.grid(row= 2, column= 2, padx= 5, pady= 5)
button_mult.grid(row= 2, column= 3, padx= 5, pady= 5)

button4.grid(row= 3, column= 0, padx= 5, pady= 5)
button5.grid(row= 3, column= 1, padx= 5, pady= 5)
button6.grid(row= 3, column= 2, padx= 5, pady= 5)
button_plus.grid(row= 3, column= 3, padx= 5, pady= 5)

button1.grid(row= 4, column= 0, padx= 5, pady= 5)
button2.grid(row= 4, column= 1, padx= 5, pady= 5)
button3.grid(row= 4, column= 2, padx= 5, pady= 5)
button_subtraction.grid(row= 4, column= 3, padx= 5, pady= 5)

button0.grid(row= 5, column= 0, columnspan= 2, padx= 5, pady= 5)
button_period.grid(row= 5, column= 2, padx= 5, pady= 5)
button_result.grid(row= 5, column= 3, padx= 5, pady= 5)





window.mainloop()