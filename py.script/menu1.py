#기본메뉴생성: pack() 등 대신에 config()를 사용

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
window=Tk()

def func_open():
    messagebox.showinfo("Open", "Select Open")
def func_exit():
    window.quit()
    window.destroy()
def func_edit():
    messagebox.showinfo("Editor", "This program was coded by 유진")
def func_ver():
    yes= messagebox.askquestion("Ask Ok/Cancel","Version 1.0 and Quit?")
    if yes == 'yes':
        window.quit()
        window.destroy()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu1=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu1)
fileMenu1.add_command(label='Open',command=func_open)
fileMenu1.add_separator()
fileMenu1.add_command(label='Exit', command=func_exit)

infoMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Info",menu=infoMenu)
infoMenu.add_command(label='Editor',command=func_edit)
infoMenu.add_separator()
infoMenu.add_command(label='Version', command=func_ver)

window.mainloop()