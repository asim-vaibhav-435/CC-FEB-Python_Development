from tkinter import *

def click(event):

    global scvalue

    text = event.widget.cget("text")
    # to take the text value of the widget
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as err:
                print(err)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        # to update the values on the screen instantly
    
root = Tk()

root.geometry("305x407")
root.title("calculator")
root.configure(background='#ffffff')
root.wm_iconbitmap("Projects/TASK1-Calculator/calculator.ico")

# screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 20 bold")
screen.configure(foreground='#003753')
screen.grid(row=0, column=0, columnspan=4)

keys = [['/', '*', '-'], ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['C', '0', '.']]

for i in range(1,6):
    for j in range(3):
        btn = Button(root, text=keys[i-1][j], width=6, height=3, font='lucida 12 bold')
        btn.configure(background="#46addd", activebackground='#ffffff', activeforeground='#1cacc4', foreground="#ffffff")
        btn.bind("<Button-1>", click)
        btn.grid(row=i, column=j)

btn_add = Button(root, text='+', width=6, height=7, font= "lucida 12 bold")
btn_add.bind("<Button-1>", click)
btn_add.configure(background="#46addd", foreground="#ffffff")
btn_add.grid(row=1, column=3, rowspan=2)

btn_equal = Button(root, text='=', width=6, height=11, font= "lucida 12 bold")
btn_equal.configure(background="#fdb111", foreground="#ffffff")
btn_equal.bind("<Button-1>", click)
btn_equal.grid(row=3, column=3, rowspan=3, columnspan=1)

root.mainloop()