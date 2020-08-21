from tkinter import *

# buat root windows
root = Tk()

# buat judul windows dan dimensi
root.title("First Project")
root.geometry('350x200')

# buat menu bar pada root windows
# item baru di menu bar dan melabelinya dengan 'new'
# buat item tambahan di menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# buat label untuk root windows
lbl = Label(root, text= "Kamu itu siapa ?")
lbl.grid()

# buat field input
txt = Entry(root, width=10)
txt.grid(column =1, row=0)

def clicked():
    res = "Kamu Tulis" + txt.get()
    lbl.configure(text = res)

# buttom widget dengan text warna merah disamping
btn = Button(root, text="Start", fg = "red", command=clicked)

btn.grid(column=2, row=0)

root.mainloop()