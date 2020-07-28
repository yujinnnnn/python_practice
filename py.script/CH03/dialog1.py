from tkinter import * 
from tkinter.simpledialog import *
 
window=Tk()
window.geometry("500x500")

label1=Label(window, text="Input value")
label1.pack() 

value=askinteger("Number","input from 1 to 6", minvalue=1, maxvalue=6)
label1.configure(text=str(value))

window.mainloop()