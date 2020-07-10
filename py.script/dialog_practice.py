from tkinter import *
class Profit:
    name=";rate 0.0; money=0; interest=0.0; total=0.0"
    def cal(self):
        self.interest= float(text1.get())
        self.money=float(text2.get())
        self.total=self.money + (self.interest*self.money)
        self.name=text3.get()
        label4.configure(text="순수익: %.2f"%self.total)
    def clear(self):
        text1.delete(0,END)
        text2.delete(0,END)
        text3.delete(0,END)
        label4.configure(text='입력하시오 : ')
def func_exit():
    window.quit()
    window.destroy()
me=Profit()

window=Tk()
window.title("interest cal")
window.geometry("350x200+800+400")
window.resizable(width=False, height=False)

label1=Label(window, text='이자율(0.1~0.6) : ')
label2=Label(window, text='입금금액 : ')
label3=Label(window, text='사용자   : ')
label4=Label(window, text='순수익')

text1 = Entry(window, bd=3, width=20)
text2 = Entry(window, bd=3, width=20)
text3 = Entry(window, bd=3, width=20)

button1 =Button(window, text='계산', fg='blue', command=me.cal)
button2 =Button(window, text='닫기', fg='blue', command=func_exit)
button3 =Button(window, text='삭제', fg='blue', command=me.clear)

label1.grid(row=1, column=1, padx=3,pady=7)
text1.grid(row=1, column=2, padx=3,pady=7)
label2.grid(row=2, column=1, padx=3,pady=7)
text2.grid(row=2, column=2, padx=3,pady=7)
label3.grid(row=3, column=1, padx=3,pady=7)
text3.grid(row=3, column=2, padx=3,pady=7)
label4.grid(row=4, column=1, padx=3,pady=7)

button1.place(x=70,y=150,height=40,width=60)
button2.place(x=140,y=150,height=40,width=60)
button3.place(x=210,y=150,height=40,width=60)

window.mainloop()