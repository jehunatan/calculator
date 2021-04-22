from tkinter import *
from tkinter import font as tkFont

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


def btn_delete():
    current_len = len(display.get())  # current length of entry
    display.delete(current_len-1)


def btn_equal():
    current_len = len(display.get())
    display.insert(current_len, "=")

    # creating a [number, operator, number, operator]-looking list
    operation = display.get()
    help_list = []
    number = ""
    for character in operation:
        if is_number(character) or character == ".":
            number += character
        elif character == "=":
            help_list.append(float(number))
        else:
            help_list.append(float(number))
            help_list.append(character)
            number = ""

    # perform only the multiplications
    for i in range(len(help_list)):
        if i > len(help_list)-1:
            break
        else:
            if help_list[i] == "x":
                result = help_list[i-1] * help_list[i+1]
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.pop(i-1)
                help_list.insert(i-1,result)

    # perform only the divisions
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

    # If the final result is an integer, not display it like a float(14.0)
    final_result = str(final_result)
    i = final_result.find(".")
    after_dot = final_result[i+1:]
    if len(after_dot) == 1 and final_result[i+1] == str(0):
        display.delete(0, END)
        display.insert(0, final_result[:-2])
    else:
        zero_count = 0
        digit_count = 0  # number of digits after the decimal dot
        for i in range(i+1, len(final_result)):
            if final_result[i] == str(0):
                zero_count += 1
            digit_count += 1
        if zero_count == digit_count:  # if the number is looking like that: 14.0000 display 14
            display.delete(0, END)
            display.insert(0, final_result[:i])
        else:  # numbers like 14.003
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
window.resizable(False, False)

my_font = tkFont.Font(family='Helvetica', size=20, weight="bold")

# Widgets
frm_display = Frame(window, padx=10, pady=20)
display = Entry(frm_display, font=my_font)
btn_7 = Button(text="7", height=2, fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(7))
btn_8 = Button(text="8",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(8))
btn_9 = Button(text="9",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(9))
btn_4 = Button(text="4", height=2, fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(4))
btn_5 = Button(text="5",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(5))
btn_6 = Button(text="6",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(6))
btn_1 = Button(text="1", height=2,fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(1))
btn_2 = Button(text="2",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(2))
btn_3 = Button(text="3",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(3))
btn_0 = Button(text="0", height=2,fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click(0))
btn_clear = Button(text="C", width=4, height=2, fg="white", bg="#4c748c", font=my_font, command=btn_clear)
btn_add = Button(text="+",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click("+"))
btn_subtract = Button(text="-",fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click("-"))
btn_equal = Button(text="=", fg="white", bg="#e68a00", font=my_font, command=btn_equal)
btn_multiply = Button(text="x", width=4, fg="white", bg="#4c748c", font=my_font, command=lambda: btn_click('x'))
btn_divide = Button(text="/", width=4, fg="white", bg="#4c748c", font=my_font, command=lambda: btn_click("/"))
btn_delete = Button(text="Del", width=4, fg="white", bg="#4c748c", font=my_font, command=btn_delete)
btn_decimal = Button(text=".", width=4, fg="white", bg="#7494ab", font=my_font, command=lambda: btn_click("."))

# Placing widgets into window
frm_display.grid(row=0, column=0, columnspan=4, sticky="nsew")
display.pack(fill=BOTH)
btn_7.grid(row=2, column=0, sticky="nsew")
btn_8.grid(row=2, column=1, sticky="nsew")
btn_9.grid(row=2, column=2, sticky="nsew")
btn_4.grid(row=3, column=0, sticky="nsew")
btn_5.grid(row=3, column=1, sticky="nsew")
btn_6.grid(row=3, column=2, sticky="nsew")
btn_1.grid(row=4, column=0, sticky="nsew")
btn_2.grid(row=4, column=1, sticky="nsew")
btn_3.grid(row=4, column=2, sticky="nsew")
btn_0.grid(row=5, column=0, columnspan=2, sticky="nsew")
btn_clear.grid(row=1, column=0, sticky="nsew")
btn_multiply.grid(row=1, column=3, sticky="nsew")
btn_subtract.grid(row=2, column=3, sticky="nsew")
btn_add.grid(row=3, column=3, sticky="nsew")
btn_divide.grid(row=1, column=2, sticky="nsew")
btn_equal.grid(row=4, column=3, rowspan=2, sticky="nsew")
btn_delete.grid(row=1, column=1, sticky="nsew")
btn_decimal.grid(row=5,column=2, sticky="nsew")

window.mainloop()
