import tkinter
import random
##########################################
def pc_stone():

##########################################
def p_to_c():
    tk_pc=tkinter.Tk()
    tk_pc.title("请开始")
    btn3=tkinter.Button(tk_pc,text="石头",command=pc_stone)
    btn4=tkinter.Button(tk_pc,text="剪刀",command=pc_cut)
    btn5=tkinter.Button(tk_pc,text="布",command=pc_cloth)
##########################################
def p_to_p():
    tk_pc.title("第一位请开始选择")
    btn6=tkinter.Button(tk_pp,text="石头",command=pp_stone)
    btn7=tkinter.Button(tk_pp,text="剪刀",command=pp_cut)
    btn8=tkinter.Button(tk_pp,text="布",command=pp_cloth)
##########################################
tk=tkinter.Tk()
tk.title("石头剪刀布")
lab1=tkinter.Lable(tk,text="请选择模式")
btn1=tkinter.Button(tk,text="人机模式",command=p_to_c)
btn2=tkinter.Button(tk,text="双人模式",command=p_to_p)