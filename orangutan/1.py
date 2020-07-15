import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import pickle

dic={}
usrName=None
psw=None

#--------登陆处理---------
def loginHandle():
    global dic
    global usrName
    global psw
    usrName=usrEntry.get()
    psw=pswEntry.get()
    dic=json2dic()
    #print(dic)
    #print(pswEntry.get())

    if dic.get(usrName)!=None and dic[usrName].get("psw")==psw:
        root.geometry("300x400")
        root.title("%s,你好！请留言"%(usrName))
        usrFrame.pack_forget()
        pswFrame.pack_forget()
        btnFrame.pack_forget()
        msgFrame.pack(side="top",fill="x")
        ttk.Separator(root,orient="horizontal").pack(fill="x")
        textScrollBar.pack(side="left",fill="y")
        msgText.pack(fill="both",expand="yes",side="left")
        for n in dic[usrName]["msg"]:
            msgText.insert("end",dic[usrName]["msg"][n])
            msgText.insert("insert","\n")
    else:
        messagebox.showerror(title="错误",message="用户或密码错误，请新输入！")
        
def creat_username():
    global usrName
    global psw
    global dic
    usrName=usrEntry.get()
    psw=pswEntry.get()
    dic=json2dic()
    print(dic)
    if len(usrName)!=0 and usrName.isspace()==False and dic.get(usrName)==None:
        if len(psw)!=0 and psw.isspace()==False:
            dic.update({usrName:{"psw":psw,"msg":{}}})
            dic2json(dic)
            messagebox.showinfo(title="恭喜你",message="创建成功！")
        else:
            messagebox.showerror(title="错误",message="密码不能为空")
    else:
        messagebox.showerror(title="错误",message="用户已存在或不符合规范，请重新输入！")

def writeMsg():
    global dic
    global usrName
    global psw
    #====判断字符串为空或全是空格=====
    if len(msgEntry.get())!=0 and msgEntry.get().isspace()==False:
        msgText.insert("end",msgEntry.get())
        dic[usrName]["msg"].update({len(dic[usrName]["msg"])+1:msgEntry.get()})   #***************关键*************
        dic2json(dic)
        print(dic)
        msgText.insert("insert","\n")
        msgEntry.delete(0,"end")
    else:
        print("wrong")
        tk.messagebox.showerror(title="错误",message="没有内容，请重新输入！")

def dic2json(dict):
    f=open("orangutan/1.txt","wb")
    pickle.dump(dict,f)
    f.close()

def json2dic():
    f=open("orangutan/1.txt","rb")
    dict=pickle.load(f)
    f.close()
    return dict


#dic2json(dic)
root=tk.Tk()
root.title("留言板")


#-------列表框---------
'''
userList=tk.Listbox(root)
user=["1","2","3","4"]
for i in user:
    userList.insert(0,i)
userList.pack()
'''


#--------root窗口界面------
usrFrame=tk.Frame(root)
usrFrame.pack(padx=10,pady=5)
usrLabel=tk.Label(usrFrame,text="用户")
usrLabel.pack(side="left",padx=5)

usrEntry=tk.Entry(usrFrame)
usrEntry.pack(side="right",fill="x",padx=5)

pswFrame=tk.Frame(root)
pswFrame.pack(padx=10,pady=5)
pswLabel=tk.Label(pswFrame,text="密码")
pswLabel.pack(side="left",padx=5)

pswEntry=tk.Entry(pswFrame)
pswEntry.pack(side="right",fill="x",padx=5)

btnFrame=tk.Frame(root)
btnFrame.pack(padx=10,pady=5)

loginBtn=tk.Button(btnFrame,text="登陆",command=loginHandle)
loginBtn.pack(side="left",padx=10)
exitBtn=tk.Button(btnFrame,text="创建",command=creat_username)
exitBtn.pack(side="right",padx=10)

#-------锁定窗口大小-----------
root.update()
root.geometry("%dx%d"%(root.winfo_width(),root.winfo_height()))


#---------登陆成功窗口---------
msgFrame=tk.Frame(root,height=1)
msgEntry=tk.Entry(msgFrame)
msgEntry.pack(side="left",expand="yes",fill="both")
msgBtn=tk.Button(msgFrame,text="留言",width=5,command=writeMsg)
msgBtn.pack(side="right")
textScrollBar=tk.Scrollbar(root)
msgText=tk.Text(root,yscrollcommand=textScrollBar.set)#滚动条绑定
textScrollBar.config(command=msgText.yview)


root.mainloop()

