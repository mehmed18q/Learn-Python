from tkinter import *


root = Tk()
root.title("limoonad")
root.config(bg='gray',width='300',height='300')
root.resizable(0,0)

button=Button(root, text='Login')
button.place(x='20',y='100')
button.config(bg='red',fg='white',width='35',height='3')

label=Label(root, text='Enter a username here: ')
label.place(x='10',y='20')
label.config(bg='gray')

label2=Label(root, text='Enter a password here: ')
label2.place(x='10',y='60')
label2.config(bg='gray')

entry=Entry(root, width='20')
entry.place(x='150',y='20')

entry2=Entry(root, width='20')
entry2.place(x='150',y='60')
entry2.config(show='*')

label3=Label(root, text='Logged in curently!!!')

label3.config(bg='yellow')

def click(event):
    a=entry.get()
    print(a)
    b=entry2.get()
    print(b)
    label3.place(x='100',y='175')
button.bind("<ButtonPress>",click)





