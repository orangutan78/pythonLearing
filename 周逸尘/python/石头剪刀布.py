import tkinter
import random
##########################################
pc_score=0
pp_score=0
##########################################
tk_owner=tkinter.Tk()
tk_owner.title("开始游戏")
btnx=tkinter.Button(tk_owner,text="开始游戏",command=start)
btnx.pack()
##########################################
def ok(a,b):
    tke=tkinter.Tk()
    tke.title(a)
    labe=tkinter.Label(tke,text=b)
    labe.pack()
    btne=tkinter.Button(tke,text="人机模式",command=p_to_c)
    btne.pack()
    btne1=tkinter.Button(tke,text="双人模式",command=p_to_p)
    btne1.pack()
##########################################
def pc_end(x):
    pc_form=random.choice([ '石头','剪刀', '布'])
    if x==1:
        if pc_form=='石头':
            ok("draw","平局")
        elif pc_form=='剪刀':
            ok("win","你赢了")
        else:
            ok("lost","你输了")
    if x==2:
        if pc_form=='石头':
            ok("lost","你输了")
        elif pc_form=='剪刀':
            ok("draw","平局")
        else:
            ok("win","你赢了")
    if x==2:
        if pc_form=='石头':
            ok("lost","你输了")
        elif pc_form=='剪刀':
            ok("draw","平局")
        else:
            ok("win","你赢了")
##########################################
def p_to_c():
    tk_pc=tkinter.Tk()
    tk_pc.title("请开始")
    btn3=tkinter.Button(tk_pc,text="石头",command=lambda:pc_end(1))
    btn4=tkinter.Button(tk_pc,text="剪刀",command=lambda:pc_end(2))
    btn5=tkinter.Button(tk_pc,text="布",command=lambda:pc_end(3))
##########################################
def p_to_p():
    tk_pp=tkinter.Tk()
    tk_pp.title("第一位请开始选择")
    btn6=tkinter.Button(tk_pp,text="石头",command=pp_stone)
    btn7=tkinter.Button(tk_pp,text="剪刀",command=pp_cut)
    btn8=tkinter.Button(tk_pp,text="布",command=pp_cloth)
##########################################
def start():
    tk=tkinter.Tk()
    tk.title("石头剪刀布")
    lab1=tkinter.Lable(tk,text="请选择模式")
    btn1=tkinter.Button(tk,text="人机模式",command=p_to_c)
    btn2=tkinter.Button(tk,text="双人模式",command=p_to_p)