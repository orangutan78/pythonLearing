import tkinter as tk
import random
import pygame as pg
import time

class Tetris:
    '俄罗斯方块'
    FPS=200         #刷新速度
    cell_size=30    #格子大小
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
        self.parent.focus_set()
        self.parent.bind("<KeyPress-Left>",self.move_horizontal)
        self.parent.bind("<KeyPress-Right>",self.move_horizontal)
        self.parent.bind("<KeyPress-Up>",self.rotation_block)
        self.parent.bind("<KeyPress-Down>",self.down_block)
        self.game_loop()
        storge_block=[[0 for i in range(self.win_c)]for i in range(self.win_r)] #创建空二维列表

    def game_loop(self):#控制时间
        global one_block
        self.parent.update()
        direction=[0,1]
        if one_block==None:
            one_block=self.generate_new_block()
        elif self.check_move(one_block,direction) and self.check_inside(one_block["pos"])==False:
            self.block_move(one_block,direction)
        else:
            self.save_block_list(one_block)
            one_block=None
        self.parent.after(self.FPS,self.game_loop)
        

    def check_line(self): #检查哪行满
        global storge_block
        full_row_number=[]
        for i in range(self.win_r):
            count=storge_block[i].count(1)
            if count>=12:
                full_row_number.append(i)
                self.del_line(full_row_number)

    def del_line(self,list):
        global storge_block
        while len(list)>0:
            li=max(list)
            for i in range(li,-1,-1):
                for j in range(self.win_c):
                    storge_block[i][j]=storge_block[i-1][j]
            list.pop(li)
                
            

    def check_inside(self,list):       #检查方块是否已在格子里
        global storge_block
        for x,y in list:
            if storge_block[y][x]:
                return True
        return False
        

    def generate_new_block(self):   #随机生成方块
        block_type=random.choice(list(self.blocks.keys()))
        x=int(self.win_c/2)
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

    def draw_block(self,block,is_block):    #画方块
        x,y=block["xy"]
        block_type=block["block_type"]
        if is_block==True:
            color=self.blocks[block_type]["color"]
        else:
            color="#333333"
        for i in range(4):
            x0=block["pos"][i][0]+x
            y0=block["pos"][i][1]+y
            self.draw_cell(x0,y0,color)

    

    def block_move(self,block,direction=[0,0]): #移动方块
        dx,dy=direction
        x,y=block["xy"]
        self.draw_block(block,False)
        x=x+dx
        y=y+dy 
        block["xy"]=(x,y)
        self.draw_block(block,True)
        one_block["xy"]=[x,y]

    def check_move(self,block,direction=[0,0]): #检查方块是否落地
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x+direction[0]
            y1=y0+y+direction[1]
            if x1<0 or x1>=self.win_c or y1>=self.win_r :
                return False
        return True

    def save_block_list(self,block):        #存落地方块位置
        global storge_block
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x
            y1=y0+y 
            storge_block[y1][x1]=1
        self.check_line()

    def move_horizontal(self,event):        #横向移动 
        global one_block
        direction=[0,0]
        if event.keysym=="Left":
            direction=[-1,0]
        elif event.keysym=="Right":
            direction=[1,0]
        else:
            return
        if self.check_move(one_block,direction):
            self.block_move(one_block,direction)

    def rotation_block(self,event): #旋转方块
        global one_block
        if one_block is None:
            return
        else:
            self.draw_block(one_block,False)
            x,y=one_block["xy"]
            block_type=one_block["block_type"]
            if event.keysym=="Up":
                rotation_list=[]
                if one_block["block_type"]!="O":
                    for x1,y1 in one_block["pos"]:
                        x2=y1
                        y2=-x1
                        xx=x+x2
                        yy=y+y2
                        if one_block[""]  


                        ######################### 
                self.draw_block(one_block,True)
        


    def down_block(self,event):
        global one_block
        global storge_block
        x,y=one_block["xy"]
        if one_block is None:
            return
        for x1,y1 in one_block["pos"]:
            dirction=[0,0]
            x2=x+x1
            y2=y+y1
            while True:
                if storge_block[x2][y2]:
                    dirction[1]+=1 
                    y2=y+y1+dirction[1]
                else:
                    break
        self.block_move(one_block,dirction)
                
            
win=tk.Tk() 
tetris=Tetris(win)
win.mainloop()
