# Only adding and subtraction

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
    current_len = len(display.get())  # current length of entry
    display.insert(current_len, str(number))


def btn_clear():
    display.delete(0, END)


def btn_equal():
    current_len = len(display.get())  # current length of entry
    display.insert(current_len, "=")
    # creating a [number, operator, number, operator]-looking list
    operation = display.get()
    help_list = []
    number = ""
    for character in operation:
        if is_number(character):
            number += character
        elif character == "=":
            help_list.append(int(number))
        else:
            help_list.append(int(number))
            help_list.append(character)
            number = ""

    for i in range(len(help_list)):
        if i > len(help_list)-1:
            break
        else:
            if help_list[i] == "*":
                result = help_list[i-1] * help_list[i+1]
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.insert(i-1,result)

    for i in range(len(help_list)):
        if i > len(help_list)-1:
            break
        else:
            if help_list[i] == "/":
                result = int(help_list[i - 1]) / int(help_list[i + 1])
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.insert(i-1, result)

    final_result = 0
    operator = ""
    for i in range(len(help_list)):
        if i == 0:  # first value always will be a number
            final_result = help_list[i]
        elif not is_number(help_list[i]):  # if it is an operator
            operator = help_list[i]
        else:
            if operator == "+":
                final_result += help_list[i]
            elif operator == "-":
                final_result -= help_list[i]
    display.delete(0, END)
    display.insert(0, final_result)

# 2. solutions(the easiest with 'eval' built-in function)
def btn_equal2():
    result = eval(display.get())
    display.delete(0, END)
    display.insert(0, result)


window = Tk()
window.title("Jonathan's Calculator")
window.iconbitmap("calculator_yv6_icon.ico")

# Widgets
display = Entry()
btn_7 = Button(text="7", width=10, height=4, command=lambda: btn_click(7))
btn_8 = Button(text="8", width=10, height=4, command=lambda: btn_click(8))
btn_9 = Button(text="9", width=10, height=4, command=lambda: btn_click(9))
btn_4 = Button(text="4", width=10, height=4, command=lambda: btn_click(4))
btn_5 = Button(text="5", width=10, height=4, command=lambda: btn_click(5))
btn_6 = Button(text="6", width=10, height=4, command=lambda: btn_click(6))
btn_1 = Button(text="1", width=10, height=4, command=lambda: btn_click(1))
btn_2 = Button(text="2", width=10, height=4, command=lambda: btn_click(2))
btn_3 = Button(text="3", width=10, height=4, command=lambda: btn_click(3))
btn_0 = Button(text="0", width=10, height=4, command=lambda: btn_click(0))
btn_clear = Button(text="Clear",width=10, height=4, command=btn_clear)
btn_add = Button(text="+", width=10, height=4, command=lambda: btn_click("+"))
btn_subtract = Button(text="-", width=10, height=4, command=lambda: btn_click("-"))
btn_equal = Button(text="=", width=10, height=4, command=btn_equal)
btn_multiply = Button(text="x", width=10, height=4, command=lambda: btn_click('*'))
btn_divide = Button(text="/", width=10, height=4, command=lambda: btn_click("/"))

# Placing widgets into window
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_multiply.grid(row=1, column=3)
btn_subtract.grid(row=2, column=3)
btn_add.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_equal.grid(row=4, column=2)

window.mainloop()
