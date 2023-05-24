from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10 )



# Defining a Button function:
# Passing a parameter through the button click function because we want that button to do something.
def button_click(number):
    #e.delete(0,END)
    current =e.get() # creating a variable.
    e.delete(0,END) # to delete everything that is in there. 
    e.insert(0,str(current) + str(number)) # we are passing it in as a string. 

def button_clear():
    e.delete(0,END)

# We are creating a global variable. 
# Making sure that when the + sign is clicked the number is cleared. 
def button_add():
    first_number = e.get()
    global f_num # f_num here is a global and we can use it outside of this function.
    global math 
    math = "addition"
    f_num = int(first_number) # Here we are making sure that the number is infact an integer. 
    e.delete(0,END)



# defining the equal button,we want it to grab a variable, this is going to grab whatever is in the text box.
# Defining the adding,substracting,dividing and multiplying mechanism.
def button_equal():
    second_number = e.get(0)
    e.delete(0,END)

    if math == "addition":
       e.insert(0,f_num + int(second_number))

    if math == "subtraction":
       e.insert(0,f_num - int(second_number))

    if math == "multiplication":
       e.insert(0,f_num * int(second_number))

    if math == "division":
       e.insert(0,f_num / int(second_number))

    



def button_substract():
    first_number = e.get()
    global f_num # f_num here is a global and we can use it outside of this function.
    global math 
    math = "subtraction"
    f_num = int(first_number) # Here we are making sure that the number is infact an integer. 
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num # f_num here is a global and we can use it outside of this function.
    global math 
    math = "multiplication"
    f_num = int(first_number) # Here we are making sure that the number is infact an integer. 
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num # f_num here is a global and we can use it outside of this function.
    global math 
    math = "division"
    f_num = int(first_number) # Here we are making sure that the number is infact an integer. 
    e.delete(0,END)



#Defining all the buttons on a calculator: we use lambda to define parameteres here. 

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)) # here if we were to type 1 as "1" then we would not change the current and number to a string above.
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_a = Button(root, text="+", padx=39, pady=20, command=button_add) # we do not need the lambda because we are not passing anything.
button_e = Button(root, text="=", padx=91, pady=20, command=lambda: button_equal())
button_clr = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subs = Button(root, text="-", padx=41, pady=20, command=button_substract)
button_multi = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_div = Button(root, text="/", padx=41, pady=20, command=button_divide)

# Putting the buttons on the screen :

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1, columnspan=2)
button_a.grid(row= 5, column=0)
button_e.grid(row=5, column=1, columnspan=2)

button_subs.grid(row= 6, column=0)
button_multi.grid(row= 6, column=1)
button_div.grid(row= 6, column=2)




root.mainloop()