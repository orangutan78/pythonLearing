import tkinter
import tkinter.messagebox
import json

##----------显示登陆------------#
def isok():
    if ent1.get()=="乜克" and ent2.get()=="mieke.mie":
        a.deiconify()  #显示窗口
        a.title("乜克窗口")
    elif ent1.get()=="乜几" and ent2.get()=="mieji.mie":
        a.deiconify()  #显示窗口
        a.title("乜几窗口")
    elif ent1.get()=="乜丁" and ent2.get()=="mieding.mie":
        a.deiconify()  #显示窗口
        a.title("乜丁窗口")
    elif ent1.get()=="乜生然" and ent2.get()=="mieshengran.mie":
        a.deiconify()  #显示窗口
        a.title("乜生然窗口")
    elif ent1.get()=="浮士德" and ent2.get()=="faust.mie":
        a.deiconify()  #显示窗口
        a.title("浮士德窗口")
    else:
        tkinter.messagebox.showerror(title="wrong",message="请重新输入")
        
#----------creat---------------#
def creat():
    dic={}
    if ent3.get()!="" and ent3.get()!=" ":
        if ent1.get()=="乜克":
            with open("majibee.dic.txt")as file_object:
                words=file_object.read()
        if ent1.get()=="乜几":
            with open("majibee.dic2.txt")as file_object:
                words=file_object.read()
        if ent1.get()=="乜丁":
            with open("majibee.dic3.txt")as file_object:
                words=file_object.read()
        if ent1.get()=="乜生然":
            with open("majibee.dic4.txt")as file_object:
                words=file_object.read()
        if ent1.get()=="浮士德":
            with open("majibee.dic5.txt")as file_object:
                words=file_object.read()            
        realWords=json.loads(words)
        for n in realWords:
            dic[n]=realWords[n]
        dic[len(dic)]=ent3.get()
        txtofdic=json.dumps(dic,ensure_ascii=False) #不以ascII码存
        if ent1.get()=="乜克":
            filename="majibee.dic.txt"
        if ent1.get()=="乜几":
            filename="majibee.dic2.txt"
        if ent1.get()=="乜丁":
            filename="majibee.dic3.txt"
        if ent1.get()=="乜生然":
            filename="majibee.dic4.txt"
        if ent1.get()=="浮士德":
            filename="majibee.dic5.txt"
        with open(filename,"w")as file_object:
            file_object.write(txtofdic)
#------------查看--------------#
def havealook():
    b=tkinter.Tk()
    b.geometry("350x600")
    if ent1.get()=="乜克":
        b.title("乜克留言版")
        with open("majibee.dic.txt")as file_object:
            words=file_object.read()
    if ent1.get()=="乜几":
        b.title("乜几留言版")
        with open("majibee.dic2.txt")as file_object:
            words=file_object.read()
    if ent1.get()=="乜丁":
        b.title("乜丁留言版")
        with open("majibee.dic3.txt")as file_object:
            words=file_object.read()
    if ent1.get()=="乜生然":
        b.title("乜生然留言版")
        with open("majibee.dic4.txt")as file_object:
            words=file_object.read()
    if ent1.get()=="浮士德":
        b.title("浮士德留言版")
        with open("majibee.dic5.txt")as file_object:
            words=file_object.read()            
    realWords=json.loads(words)
    t1=tkinter.Text(b)
    t1.pack()
    for n in realWords:
        #tkinter.Text(b,text=realWords[n]).pack()
        t1.insert("end",realWords[n]) 
        t1.insert("insert","\n") 
        
##-------------------程序开始-----------------#
dic={}
majibee=tkinter.Tk()
#题目=乜几B-majibee#
majibee.title("乜几B-majibee")
majibee.geometry("280x150")
#----------majibee标签------------#
lab1=tkinter.Label(text="请输入你的majibee帐号")
lab1.pack()
#----------majibee输入框------------#
ent1=tkinter.Entry()
ent1.pack()
#----------majibee标签------------#
lab2=tkinter.Label(text="请输入你的majibee密码")
lab2.pack()
#----------majibee输入框2-----------#
ent2=tkinter.Entry(show="乜")
ent2.pack()
#----------majibee确定--------------#
btn1=tkinter.Button(text="登陆",command=isok)
btn1.pack()
#----------majibee退出--------------#
btn2=tkinter.Button(text="退出",command=majibee.quit)
btn2.pack()
#--------登陆成功窗口------#
a=tkinter.Toplevel()
a.withdraw()    #隐藏窗口#
a.geometry("250x100")
lab3=tkinter.Label(a,text="请输入你的创建内容")
lab3.pack()
ent3=tkinter.Entry(a)
ent3.pack()
btn5=tkinter.Button(a,text="创建",command=creat)       
btn5.pack()
btn6=tkinter.Button(a,text="查看",command=havealook)
btn6.pack()
#----------majibee加强化设置----------#
majibee.mainloop()
