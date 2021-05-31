import tkinter
import tkinter.messagebox


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


root = tkinter.Tk(className='hello')
root.geometry('250x150')
label = tkinter.Label(root, text='Hello World!', font='Helvetica -14 bold')
btn = tkinter.Button(root, text='QUIT',
                     command=lambda: tkinter.messagebox.showinfo('Info', '确定要退出吗'),
                     activebackground='red', activeforeground='white')
scale = tkinter.Scale(root, from_=10, to=40, command=resize, orient=tkinter.HORIZONTAL)
scale.set(14)
label.pack(fill=tkinter.Y, expand=1)
scale.pack(fill=tkinter.X, expand=1)
btn.pack()
tkinter.mainloop()
