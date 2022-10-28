from tkinter import *
import math
from math import sqrt

expression=""

def press(num):
    
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=total
    except:
        equation.set('error')
        expression=""

def delete():
    global expression   
    length=expression_field.get()[0:-1]
    expression_field.delete(0,"end")
    expression_field.insert(0,length)
    expression=length
    

def clear(): 
    global expression 
    expression = "" 
    equation.set("")

window=Tk()

window.geometry('340x320')
window.title("Calculator")
window.resizable(0,0)
window.configure(bg='black')


equation=StringVar()
expression_field=Entry(window,textvariable=equation,bg="BLACK",fg="#FFFFFF")
expression_field.grid(columnspan=8, ipadx=110,)

button7=Button(window, text="7",width=4,height=2,command=lambda: press(7),fg="#FFFFFF",bg="BLACK")
button7.place(x=30, y=60)
button8=Button(window,text="8",width=4,height=2,command=lambda: press(8),fg="#FFFFFF",bg="BLACK")
button8.place(x=80,y=60)
button9=Button(window,text="9",width=4,height=2,command=lambda: press(9),fg="#FFFFFF",bg="BLACK")
button9.place(x=130,y=60)

buttondiv=Button(window, text="/",width=4,height=2,command=lambda: press("/"),fg="#FFFFFF",bg="#333333")
buttondiv.place(x=180, y=60)
buttonsqrroot=Button(window,text="√",width=4,height=2,command=lambda: press("sqrt("),fg="#FFFFFF",bg="#333333")
buttonsqrroot.place(x=230,y=60)
buttonclear=Button(window,text="clear",width=4,height=2,command=clear,fg="#FFFFFF",bg="#333333")
buttonclear.place(x=280,y=60)

button4=Button(window, text="4",width=4,height=2,command=lambda: press(4),fg="#FFFFFF",bg="BLACK")
button4.place(x=30, y=110)
button5=Button(window,text="5",width=4,height=2,command=lambda: press(5),fg="#FFFFFF",bg="BLACK")
button5.place(x=80,y=110)
button6=Button(window,text="6",width=4,height=2,command=lambda: press(6),fg="#FFFFFF",bg="BLACK")
button6.place(x=130,y=110)

buttonmul=Button(window,text="x",width=4,height=2,command=lambda: press("*"),fg="#FFFFFF",bg="#333333")
buttonmul.place(x=180,y=110)
buttonper=Button(window,text="%",width=4,height=2,command=lambda: press("/100"),fg="#FFFFFF",bg="#333333")
buttonper.place(x=230,y=110)
buttondel=Button(window,text="Del",width=4,height=2,command=delete,fg="#FFFFFF",bg="#333333")
buttondel.place(x=280,y=110)

button1=Button(window, text="1",width=4,height=2,command=lambda: press(1),fg="#FFFFFF",bg="BLACK")
button1.place(x=30, y=160)
button2=Button(window,text="2",width=4,height=2,command=lambda: press(2),fg="#FFFFFF",bg="BLACK")
button2.place(x=80,y=160)
button3=Button(window,text="3",width=4,height=2,command=lambda: press(3),fg="#FFFFFF",bg="BLACK")
button3.place(x=130,y=160)

buttonsub=Button(window,text="-",width=4,height=2,command=lambda: press("-"),fg="#FFFFFF",bg="#333333")
buttonsub.place(x=180,y=160)
buttonsqr=Button(window,text="x²",width=4,height=2,command=lambda: press("**2"),fg="#FFFFFF",bg="#333333")
buttonsqr.place(x=230,y=160)
buttonpi=Button(window,text="π",width=4,height=2,command=lambda: press("*3.14"),fg="#FFFFFF",bg="#333333")
buttonpi.place(x=280,y=160)

button0=Button(window, text="0",width=4,height=2,command=lambda: press(0),fg="#FFFFFF",bg="BLACK")
button0.place(x=30, y=210)
buttondot=Button(window,text=".",width=4,height=2,command=lambda: press("."),fg="#FFFFFF",bg="BLACK")
buttondot.place(x=80,y=210)
buttoneq=Button(window,text="=",width=4,height=2,command=equalpress,fg="#FFFFFF",bg="BLACK")
buttoneq.place(x=130,y=210)

buttonadd=Button(window,text="+",width=4,height=2,command=lambda: press("+"),fg="#FFFFFF",bg="#333333")
buttonadd.place(x=180,y=210)
buttonpi=Button(window,text="π",width=4,height=2,command=lambda: press("*3.14"),fg="#FFFFFF",bg="#333333")
buttonpi.place(x=280,y=160)
buttonbrace1=Button(window,text="(",width=4,height=2,command=lambda: press("("),fg="#FFFFFF",bg="#333333")
buttonbrace1.place(x=230,y=210)
buttonbrace2=Button(window,text=")",width=4,height=2,command=lambda: press(")"),fg="#FFFFFF",bg="#333333")
buttonbrace2.place(x=280,y=210)


window.mainloop()