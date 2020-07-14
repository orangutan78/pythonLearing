#########画美化方块#####
import tkinter
tk=tkinter.Tk()
canvas=tkinter.Canvas(tk,width=400,height=400)
canvas.pack()
color=["#3e7dff","#2313b9","#160a6f"]
color=["#2fe7b9","#0b7b7a","#064141"]
color=["#f29086","#ba483d","#5d150d"]
color=["#d2a0eb","#8941af","#4e156b"]
color=["#e3ab89","#aa6237","#663112"]
color=["#deea00","#8f9600","#363900"]
color=["#ef99e0","#a53a92","#611353"]

canvas.create_polygon(0,30,0,0,30,0,23,7,7,7,7,23,fill=color[0],width=0)
canvas.create_rectangle(7,7,23,23,fill=color[1],width=0)
canvas.create_polygon(30,0,30,30,0,30,7,23,23,23,23,7,fill=color[2],width=0) 

tk.update()
tk.mainloop()