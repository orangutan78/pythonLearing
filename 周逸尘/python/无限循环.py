import tkinter
####################################
def start():
    tk1=tkinter.Tk()
    tk1.geometry("300x300")
    lab2=tkinter.Label(tk1,text="已开始新的循环")
    lab2.pack()
    btn2=tkinter.Button(tk1,text="继续",command=start)
    btn2.pack()
####################################
tk=tkinter.Tk()
tk.title("请开始无限循环")
tk.geometry("300x300")
lab1=tkinter.Label(tk,text="请开始")
lab1.pack()
btn1=tkinter.Button(tk,text="开始",command=start)
btn1.pack()
####################################
tk.mainloop()