from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value= "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("Calculator By Samarpit")
root.wm_iconbitmap("icon.png")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="8", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="7", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="5", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="4", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="2", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="1", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=4.5, pady=2, font="lucida 28 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="-", padx=8, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="*", padx=11.5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="/", padx=3, pady=2, font="lucida 36 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="%", padx=3, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="=", padx=3, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text=".", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="()", padx=5, pady=2, font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()