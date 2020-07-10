import tkinter as tk
import random
import pygame as pg
import time

class Tetris:
    '俄罗斯方块'
    FPS=500
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
    one_block={
            "block_type":"T",
            "pos":blocks["T"]["pos"],
            "xy":(8,1)
        }      
    
    def __init__(self,parent):
        self.parent=parent 
                     #构造函数
        self.win_c=12
        self.win_r=20 
        self.parent.title("Tetris")
        width=self.win_c*Tetris.cell_size
        height=self.win_r*Tetris.cell_size       
        self.canvas=tk.Canvas(win,width=width,height=height)
        self.canvas.pack() 
        self.draw_bg()
        self.draw_block(1,3,"O",True)
        self.draw_block(6,3,"L",True)
        self.draw_block(3,8,"J",True)
        self.draw_block(6,8,"I",True)
        self.draw_block(3,13,"S",True)
        self.draw_block(8,13,"Z",True)
        self.draw_block(8,1,"T",True)
        self.game_loop()
        
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
        self.parent.update()
        down=[0,1]
        self.block_move(self.one_block,down)
        self.parent.after(self.FPS,self.game_loop)
    def block_move(self,block,direction=[0,0]):
        dx,dy=direction
        block_type=block["block_type"]
        x,y=block["xy"]
        block_list=block["pos"]
        self.draw_block(x,y,block_type,False)
        x=x+dx
        y=y+dy 
        self.draw_block(x,y,block_type,True)
        block["xy"]=[x,y]

win=tk.Tk() 
tetris=Tetris(win)
win.mainloop()
