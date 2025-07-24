import tkinter as tk
from tkinter import *

# To create a window or root wigdet
root=Tk()
root.title("calculator")
e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=4 ,padx =10, pady=10,)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))
    return 


# # Function to clear the input field
def button_clear():
    e.delete(0,END)
    return 

# # Function to perform summation of numbers
def button_add():
    first_num = e.get()
    global f_num
    global math
    math="add"
    if '.' in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0,END)
    return

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math="subtract"
    f_num = int(first_num)
    e.delete(0,END)
    return

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math="multiply"
    f_num = int(first_num)
    e.delete(0,END)
    return

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math="divide"
    f_num = int(first_num)
    e.delete(0,END)
    return


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    

    match math:
        case "add":
            e.insert(0, f_num+int(second_number))

        case "subtract":
            e.insert(0, f_num-int(second_number))

        case "multiply":
            e.insert(0, f_num*int(second_number))

        case "divide":
            e.insert(0, f_num/int(second_number))

# Define buttons
button1=Button(root,text='7',width=10,height=5,command = lambda: button_click(7))
button2=Button(root,text='8',width=10,height=5,command = lambda: button_click(8))
button3=Button(root,text='9',width=10,height=5,command = lambda: button_click(9))

button4=Button(root,text='4',width=10,height=5,command = lambda: button_click(4))
button5=Button(root,text='5',width=10,height=5,command = lambda: button_click(5))
button6=Button(root,text='6',width=10,height=5,command = lambda: button_click(6))

button9=Button(root,text='1',width=10,height=5,command = lambda: button_click(1))
button10=Button(root,text='2',width=10,height=5,command = lambda: button_click(2))
button11=Button(root,text='3',width=10,height=5,command = lambda: button_click(3))
button13=Button(root,text='0',width=10,height=5,command = lambda: button_click(0))

button_module=Button(root,text='%',width=10,height=5)
button_decimal=Button(root,text='.',width=10,height=5,command = lambda: button_click('.'))
button_clear=Button(root,text='clear',width=35,height=5, command = button_clear)
button_multiply=Button(root,text='*',width=10,height=5,command=button_multiply)
button_divide=Button(root,text='/',width=10,height=5,command=button_divide)
button_equal=Button(root,text='=',width=10,height=5,command=button_equal)
button_add=Button(root,text='+',width=10,height=5, command = button_add)
button_sub=Button(root,text='-',width=10,height=5,command= button_subtract)
#Placing buttons on the screen
button_module.grid(row=4,column=3)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button_multiply.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)
button9.grid(row=3,column=0)
button10.grid(row=3,column=1)
button11.grid(row=3,column=2)
button_add.grid(row=3,column=3)
button13.grid(row=4,column=0)
button_divide.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_decimal.grid(row=4,column=3)
button_clear.grid(row = 5, column = 0, columnspan=4)



root.mainloop()





