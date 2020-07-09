import tkinter
import tkinter.messagebox
import json
import pickle
score=90
dicc={}
win=tkinter.Tk()
win.title("选择特征")
win.geometry("240x1050+500+0")
a=tkinter.IntVar()
b=tkinter.IntVar()
c=tkinter.IntVar()
d=tkinter.IntVar()
e=tkinter.IntVar()
f=tkinter.IntVar()
g=tkinter.IntVar()
h=tkinter.IntVar()
a.set(0)
b.set(0)
c.set(0)
d.set(0)
e.set(0)
f.set(0)
g.set(0)
h.set(0)
def look():
    global score
    lookin=tkinter.Tk()
    lookin.title("档案")
    if a.get()==1:
        aa="男"
    elif a.get()==2:
        aa="女"
    if b.get()==1:
        bb="外向"
        score=score+1
    elif b.get()==2:
        bb="内向"
    if c.get()==1:
        cc="乐于与你交往"
        score=score+2
    elif c.get()==2:
        cc="与你交往一般"
    elif c.get()==3:
        cc="不乐于与你交往"
        score=score-2
    if d.get()==1:
        dd="极高"
        score=score+2
    elif d.get()==2:
        dd="高"
        score=score+1
    elif d.get()==3:
        dd="中等"
    elif d.get()==4:
        dd="一般"
        score=score-1
    elif d.get()==5:
        dd="差"
        score=score-2
    if d.get()==1:
        dd="深"
        score=score+3
    dicc="姓名:%s\n性别:%s\n性格类型:%s\n交往:%s\n颜值:%s\n与你的互相了解程度:%s\n助人品质:%s\n包容品质:%s\n成绩:%s\n"%(ent1.get(),aa,bb,cc,dd,ee,ff,gg,hh)
    labonline=tkinter.Text(lookin)
    labonline.insert("end",dicc)
    labonline.pack()
def isok():
    okay=tkinter.Tk()
    okay.title("成功")
    labin=tkinter.Label(okay,text="请到新窗口查看并复制")
    labin.pack()
    okay.geometry("200x100")
    anniu=tkinter.Button(okay,text="前往",command=look)
    anniu.pack()
labx=tkinter.Label(win,text="name")
labx.pack()
ent1=tkinter.Entry()
ent1.pack()
lab1=tkinter.Label(win,text="性别                                                   ")
lab1.pack()
sb1=tkinter.Radiobutton(win,text="男",variable=a,value=1)
sb2=tkinter.Radiobutton(win,text="女",variable=a,value=2)
sb1.pack()
sb2.pack()
lab2=tkinter.Label(win,text="性格1                                                 ")
lab2.pack()
sb3=tkinter.Radiobutton(win,text="外向",variable=b,value=1)
sb5=tkinter.Radiobutton(win,text="内向",variable=b,value=2)
sb3.pack()
sb5.pack()
lab3=tkinter.Label(win,text="性格2                                                 ")
lab3.pack()
sb6=tkinter.Radiobutton(win,text="乐于与你交往",variable=c,value=1)
sb7=tkinter.Radiobutton(win,text="与你交往一般",variable=c,value=2)
sb8=tkinter.Radiobutton(win,text="不乐于与你交往",variable=c,value=3)
sb6.pack()
sb7.pack()
sb8.pack()
lab4=tkinter.Label(win,text="颜值                                                  ")
lab4.pack()
sb9=tkinter.Radiobutton(win,text="极高",variable=d,value=1)
sb10=tkinter.Radiobutton(win,text="高",variable=d,value=2)
sb11=tkinter.Radiobutton(win,text="中",variable=d,value=3)
sb12=tkinter.Radiobutton(win,text="一般",variable=d,value=4)
sb13=tkinter.Radiobutton(win,text="差",variable=d,value=5)
sb9.pack()
sb10.pack()
sb11.pack()
sb12.pack()
sb13.pack()
lab5=tkinter.Label(win,text="与你的互相了解程度                                 ")
lab5.pack()
sb14=tkinter.Radiobutton(win,text="极深",variable=e,value=1)
sb15=tkinter.Radiobutton(win,text="深",variable=e,value=2)
sb16=tkinter.Radiobutton(win,text="中",variable=e,value=3)
sb17=tkinter.Radiobutton(win,text="浅",variable=e,value=4)
sb18=tkinter.Radiobutton(win,text="几乎没有",variable=e,value=5)
sb14.pack()
sb15.pack()
sb16.pack()
sb17.pack()
sb18.pack()
lab6=tkinter.Label(win,text="乐于助人                                               ")
lab6.pack()
sb19=tkinter.Radiobutton(win,text="极符合",variable=f,value=1)
sb20=tkinter.Radiobutton(win,text="符合",variable=f,value=2)
sb21=tkinter.Radiobutton(win,text="中",variable=f,value=3)
sb22=tkinter.Radiobutton(win,text="不符合",variable=f,value=4)
sb23=tkinter.Radiobutton(win,text="完全不符合",variable=f,value=5)
sb19.pack()
sb20.pack()
sb21.pack()
sb22.pack()
sb23.pack()
lab7=tkinter.Label(win,text="包容你                                                    ")
lab7.pack()
sb24=tkinter.Radiobutton(win,text="符合",variable=g,value=1)
sb26=tkinter.Radiobutton(win,text="中",variable=g,value=2)
sb28=tkinter.Radiobutton(win,text="不符合",variable=g,value=3)
sb24.pack()
sb26.pack()
sb28.pack()
lab8=tkinter.Label(win,text="成绩                                                      ")
lab8.pack()
sb29=tkinter.Radiobutton(win,text="好",variable=h,value=1)
sb30=tkinter.Radiobutton(win,text="中",variable=h,value=2)
sb31=tkinter.Radiobutton(win,text="坏",variable=h,value=3)
sb29.pack()
sb30.pack()
sb31.pack()
btn1=tkinter.Button(text="确定",command=isok)
btn1.pack()


win.mainloop()
