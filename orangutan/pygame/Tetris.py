import tkinter as tk
import random
import pygame as pg
import time

class Tetris:
    '俄罗斯方块'
    FPS=50
    cell_size=30
    blocks={
        "O":{"pos":[(-1,-1),(0,-1),(-1,0),(0,0)],"color":"blue"},
            "L":{"pos":[(0,-2),(0,-1),(0,0),(1,0)],"color":"red"},
            "J":{"pos":[(0,-2),(0,-1),(0,0),(-1,0)],"color":"orange"},
            "I":{"pos":[(0,-2),(0,-1),(0,0),(0,1)],"color":"pink"},
            "S":{"pos":[(1,-1),(0,-1),(0,0),(-1,0)],"color":"green"},
            "Z":{"pos":[(-1,-1),(0,-1),(0,0),(1,0)],"color":"brown"},
            "T":{"pos":[(-1,0),(0,0),(1,0),(0,1)],"color":"cyan"},
    }
    
    def __init__(self,parent):#构造函数
        global one_block
        global storge_block
        storge_block=[]
        one_block=None
        self.parent=parent 
        self.win_c=12
        self.win_r=20 
        self.parent.title("Tetris")
        width=self.win_c*Tetris.cell_size
        height=self.win_r*Tetris.cell_size       
        self.canvas=tk.Canvas(win,width=width,height=height)
        self.canvas.pack() 
        self.draw_bg()
        self.game_loop()

    def generate_new_block(self):#随机生成方块
        block_type=random.choice(list(self.blocks.keys()))
        x=self.win_c/2
        y=0
        global one_block
        one_block={
            "block_type":block_type,
            "pos":self.blocks[block_type]["pos"],
            "xy":(x,y)
        } 
        return one_block

    def draw_bg(self):                      #绘制背景
        for i in range(self.win_r):
            for j in range(self.win_c):  
                self.draw_cell(j,i)  
    def draw_cell(self,x,y,color="#333333"):#绘制一个格子
        x0=x*self.cell_size
        y0=y*self.cell_size
        x1=x*self.cell_size+self.cell_size
        y1=y*self.cell_size+self.cell_size
        self.canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline="#444444",width=2)

    def draw_block(self,x,y,block_type,is_block):    #按种类绘制方块
        if is_block==True:
            color=self.blocks[block_type]["color"]
        else:
            color="#333333"
        for i in range(4):
            x0=self.blocks[block_type]["pos"][i][0]+x
            y0=self.blocks[block_type]["pos"][i][1]+y
            self.draw_cell(x0,y0,color)

    def game_loop(self):#控制时间
        global one_block
        self.parent.update()
        down=[0,1]
        if one_block==None:
            one_block=self.generate_new_block()
        elif self.check_move(one_block,down):
            self.block_move(one_block,down)
        else:
            self.save_block_list(one_block)
            one_block=None
        self.parent.after(self.FPS,self.game_loop)

    def block_move(self,block,direction=[0,0]): #移动方块
        dx,dy=direction
        block_type=block["block_type"]
        x,y=block["xy"]
        #block_list=block["pos"]
        self.draw_block(x,y,block_type,False)
        x=x+dx
        y=y+dy 
        self.draw_block(x,y,block_type,True)
        one_block["xy"]=[x,y]

    def check_move(self,block,direction=[0,0]): #检查方块是否落地
        global storge_block
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x+direction[0]
            y1=y0+y+direction[1]
            if x1<0 or x1>=self.win_c or y1>=self.win_r :
                return False
            if (x1,y1) in storge_block:
                return False
        return True
    def save_block_list(self,block):
        global storge_block
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x
            y1=y0+y 
            storge_block.append((x1,y1))

win=tk.Tk() 
tetris=Tetris(win)
win.mainloop()
