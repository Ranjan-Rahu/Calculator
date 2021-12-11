from tkinter import *
from typing import Sized

root = Tk()
root.geometry('365x413')
root.title('Calculator')
root.minsize(365,413)
root.maxsize(365,413)

text_variable = StringVar()
text_variable.set('')

entry=Entry(root,textvariable=text_variable,font='lucida 30 bold',bg='black',fg='white',border=5,relief=SUNKEN)
entry.pack(fill=X)

def click(event):
    global text_variable
    text=event.widget.cget('text')
    if text=='=':
        if text_variable.get().isdigit():
            value=int(text_variable.get())
        else:
            try :
                value=eval(entry.get())
            except Exception as e:
                print(e)
                value='ERROR'
        text_variable.set(value)
        entry.update()
        
    elif text=='C':
        text_variable.set('')
        entry.update()
    else:
        text_variable.set(f'{text_variable.get()}'+f'{text}')
        entry.update()



frame= Frame(root,bg='grey',borderwidth=6)
frame.pack(side=TOP,fill=BOTH)
b1=Button(frame,text=7,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>',click)
b2=Button(frame,text=8,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>',click)
b3=Button(frame,text=9,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>',click)
b4=Button(frame,text='*',padx=10,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>',click)


frame= Frame(root,bg='grey',borderwidth=6)
frame.pack(side=TOP,fill=BOTH)
b1=Button(frame,text=4,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>',click)
b2=Button(frame,text=5,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>',click)
b3=Button(frame,text=6,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>',click)
b4=Button(frame,text='-',padx=12,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>',click)


frame= Frame(root,bg='grey',borderwidth=6)
frame.pack(side=TOP,fill=BOTH)
b1=Button(frame,text=1,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>',click)
b2=Button(frame,text=2,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>',click)
b3=Button(frame,text=3,padx=5,pady=0,font='lucida 30 bold',bg='black',fg='white')
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>',click)
b4=Button(frame,text='+',padx=8,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>',click)


frame= Frame(root,bg='grey',borderwidth=6)
frame.pack(side=TOP,fill=BOTH)
b1=Button(frame,text='/',padx=11,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>',click)
b2=Button(frame,text=0,padx=7,pady=0,font='lucida 30 bold',bg='black',fg='white')
b2.pack(side=LEFT,padx=6)
b2.bind('<Button-1>',click)
b3=Button(frame,text='C',padx=3,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>',click)
b4=Button(frame,text='=',padx=8,pady=0,font='lucida 30 bold',bg='blue',fg='white')
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>',click)


root.mainloop()