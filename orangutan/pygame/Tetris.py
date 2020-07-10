import tkinter as tk
import random
import pygame as pg

class Tetris:
    '俄罗斯方块'
    cell_size=30
    block_list={"O":{"pos":[(-1,-1),(0,-1),(-1,0),(0,0)],"color":"blue"},
                "L":{"pos":[(0,-2),(0,-1),(0,0),(1,0)],"color":"red"}
    }
    
    def __init__(self,parent):              #构造函数
        self.win_c=12
        self.win_r=20 
        width=self.win_c*Tetris.cell_size
        height=self.win_r*Tetris.cell_size       
        self.canvas=tk.Canvas(win,width=width,height=height)
        self.canvas.pack() 
        self.draw_bg()
        self.draw_block(3,3,"O")
        self.draw_block(6,3,"L")
    def draw_bg(self):                      #绘制背景
        for i in range(self.win_r):
            for j in range(self.win_c):  
                self.draw_cell(j,i)  
    def draw_cell(self,x,y,color="#cccccc"):#绘制一个格子
        x0=x*Tetris.cell_size
        y0=y*Tetris.cell_size
        x1=x*Tetris.cell_size+Tetris.cell_size
        y1=y*Tetris.cell_size+Tetris.cell_size
        self.canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline="white",width=2)
    def draw_block(self,x,y,block_type):
        color=self.block_list[block_type]["color"]
        for i in range(4):
            x0=self.block_list[block_type]["pos"][i][0]+x
            y0=self.block_list[block_type]["pos"][i][1]+y
            print(x0,y0)
            self.draw_cell(x0,y0,color)

win=tk.Tk()        
tetris=Tetris(win)
win.mainloop()
