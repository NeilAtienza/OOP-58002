#TUI form
#def main():
    # Find the least number among three numbers
   # L = []
   # num1 = eval(input("Enter the first number:"))
   # L.append(num1)
   # num2 = eval(input("Enter the second number:"))
   # L.append(num2)
   # num3 = eval(input("Enter the third number:"))
   # L.append(num3)
   # print("The smallest number among the three is:",str(min(L)))
#main()

from tkinter import *

window = Tk()
window.title("Find the Least number")
window.geometry("800x700+20+10")

def findLeast():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfLeast.set(min(L))

lbl1 = Label(window, text = "The Least Number Finder")
lbl1.grid(row=2, column=4, columnspan=4, sticky=EW)
lbl2 = Label(window, text = "Enter the first number:")
lbl2.grid(row=3, column = 3, sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.grid(row=3, column = 4)
lbl3 = Label(window,text = "Enter the second number:")
lbl3.grid(row=4, column=3)
conOfent3=StringVar()
ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.grid(row=4,column=4)
lbl4 = Label(window,text="Enter the third number:")
lbl4.grid(row=5,column =3, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.grid(row=5, column=4)

btn1 = Button(window,text = "Find the Least Number.",command=findLeast)
btn1.grid(row=6, column = 4)
lbl5 = Label(window,text="The Least number is:")
lbl5.grid(row=7,column=3,sticky=W)
conOfLeast = StringVar()
ent5 = Entry(window,bd=3,state="readonly",textvariable=conOfLeast)
ent5.grid(row=7,column=4)


mainloop()