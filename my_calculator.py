from tkinter import *

# Checks the given string if it's a number
def is_number(string):
    try:
        int(string)
    except:
        return False
    else:
        return True

def btn_click(number):
    current_len = len(display.get()) # current length of entry
    display.insert(current_len, str(number))

def btn_clear():
    display.delete(0,END)

def btn_equal():
    current_len = len(display.get()) # current length of entry
    display.insert(current_len, "=")
    # creating a [number, operator, number, operator]-looking list
    operation = display.get()
    help_list = []
    number = ""
    for character in operation:
        if is_number(character):
            number += character
        elif character == "=":
            help_list.append(number)
        else:
            help_list.append(number)
            help_list.append(character)
            number = ""

    # Computing the final result from our list
    result = 0
    operator = ""
    for i in range(len(help_list)):
        if i == 0: # first value always will be a number
            result = int(help_list[i])
        elif not is_number(help_list[i]): # if it is an operator
            operator = help_list[i]
        else:
            if operator == "+":
                result += int(help_list[i])
            elif operator == "-":
                result -= int(help_list[i])
    display.delete(0,END)
    display.insert(0,result)

# GUI settings
window = Tk()
window.title("Jonathan's Calculator")

display = Entry()
display.grid(row=0, column=0, columnspan=3, sticky="nsew",padx=10, pady=10)

btn_7 = Button(text="7", width=10, height=4, command=lambda: btn_click(7))
btn_7.grid(row=1, column=0)

btn_8 = Button(text="8", width=10, height=4, command=lambda: btn_click(8))
btn_8.grid(row=1, column=1)

btn_9 = Button(text="9", width=10, height=4, command=lambda: btn_click(9))
btn_9.grid(row=1, column=2)

btn_4 = Button(text="4", width=10, height=4, command=lambda: btn_click(4))
btn_4.grid(row=2, column=0)

btn_5 = Button(text="5", width=10, height=4, command=lambda: btn_click(5))
btn_5.grid(row=2, column=1)

btn_6 = Button(text="6", width=10, height=4, command=lambda: btn_click(6))
btn_6.grid(row=2, column=2)

btn_1 = Button(text="1", width=10, height=4, command=lambda: btn_click(1))
btn_1.grid(row=3, column=0)

btn_2 = Button(text="2", width=10, height=4, command=lambda: btn_click(2))
btn_2.grid(row=3, column=1)

btn_3 = Button(text="3", width=10, height=4, command=lambda: btn_click(3))
btn_3.grid(row=3, column=2)

btn_0 = Button(text="0", width=10, height=4, command=lambda: btn_click(0))
btn_0.grid(row=4, column=0)

btn_clear = Button(text="Clear", command=btn_clear)
btn_clear.grid(row=4, column=1, columnspan=2,  sticky="nsew")

btn_add = Button(text="+", width=10, height=4, command=lambda: btn_click("+"))
btn_add.grid(row=5, column=0)

btn_subtract = Button(text="-", width=10, height=4, command=lambda: btn_click("-"))
btn_subtract.grid(row=5, column=1)

btn_equal = Button(text="=", command=btn_equal)
btn_equal.grid(row=5, column=2, sticky="nsew")

window.mainloop()