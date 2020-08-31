from tkinter import *
from math import *
root =Tk()
root.title("CALCULATOR")
e= Entry(root , width = 55, borderwidth=5)
e.grid(row=0 , column=0,columnspan=4,padx=20,pady=20)
def button_click(num):
    #e.delete(0,END)
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))
 
def button_clear():
    e.delete(0,END)
    
def button_add():

    f_num= e.get()
    global fu_num
    global math
    math = "addition"
    fu_num=float(f_num)
    e.delete(0,END)


def button_sub():
    f_num= e.get()
    global fu_num
    global math
    math = "subtraction"
    fu_num=float(f_num)
    e.delete(0,END)
    
def button_mul():
    f_num= e.get()
    global fu_num
    global math
    math = "multiplication"
    fu_num=float(f_num)
    e.delete(0,END)
    
def button_div():
    f_num= e.get()
    global fu_num
    global math
    math = "division"
    fu_num=float(f_num)
    e.delete(0,END) 
    
def button_pow():
    f_num= e.get()
    global fu_num
    global math
    math = "power"
    fu_num=float(f_num)
    e.delete(0,END)    
    
    
def button_equal():
    s_num=e.get()
    e.delete(0,END)
    
    if math=="addition":
        e.insert(0,fu_num+float(s_num))
    if math=="multiplication":
        e.insert(0,fu_num * float(s_num))
    if math=="division":
        e.insert(0,fu_num/float(s_num))
    if math=="subtraction":
        e.insert(0,fu_num-float(s_num))
    if math=="power":
        e.insert(0,pow(fu_num,float(s_num)))    
        
    
    
    
    

button_1 = Button(root , text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root , text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root , text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root , text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root , text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root , text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root , text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root , text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root , text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(root , text="0",padx=40,pady=20,command=lambda:button_click(0))
button_add = Button(root , text="+",padx=39,pady=20,command=button_add)
button_sub = Button(root , text="-",padx=40,pady=20,command=button_sub)
button_mul = Button(root , text="*",padx=40,pady=20,command=button_mul)
button_div = Button(root , text="/",padx=40,pady=20,command=button_div)
button_clear = Button(root , text="clear",padx=80,pady=20,command=button_clear)
button_equal = Button(root , text="=",padx=88,pady=20,command=button_equal)
button_dot = Button(root , text=".",padx=41,pady=20,command=lambda:button_click("."))
button_pow = Button(root , text="^",padx=40,pady=20,command=button_pow)

button_1.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=0)
button_4.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=0)
button_7.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=0)
button_0.grid(row=4,column=1)
button_equal.grid(row=5,column=0,columnspan=2)
button_add.grid(row=4,column=3)
button_clear.grid(row=5,column=2,columnspan=2)
button_mul.grid(row=2,column=3)
button_sub.grid(row=1,column=3)
button_div.grid(row=3,column=3)
button_dot.grid(row=4,column=2)
button_pow.grid(row=4,column=0)




root.mainloop()

