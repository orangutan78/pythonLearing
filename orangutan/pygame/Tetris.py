import tkinter as tk
import random
import pygame as pg
import time

class Tetris:
    '俄罗斯方块'
    FPS=1000         #刷新速度
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
        self.win_c=12
        self.win_r=20 
        self.score=0
        self.line_number=0
        storge_block=[["" for i in range(self.win_c)]for i in range(self.win_r)] #创建空二维列表
        one_block=None
        self.parent=parent 
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

    def game_loop(self):#控制时间
        global one_block
        self.parent.title("Tetris:SCORES:%s" %self.score)
        self.difficult()
        self.parent.update()
        direction=[0,1]
        if self.check_game_over()==False:
            if one_block==None:
                one_block=self.generate_new_block()
            elif self.check_move(one_block,direction) :
                self.block_move(one_block,direction)
            else:
                self.save_block_list(one_block)
                one_block=None
            self.parent.after(self.FPS,self.game_loop)
        else:
            print("game over")
    
    def difficult(self):   #方块掉落速度变更
        if self.line_number==0:
            self.FPS=1000
        else:
            self.FPS =1000//self.line_number
        

    def check_game_over(self): #游戏结束
        global storge_block
        for i in storge_block[0]:
            if i:
                return True
        return False

    def check_line(self): #检查哪行满
        global storge_block
        full_row_number=[]
        for i in range(self.win_r):
            count=0
            for j in range(self.win_c):
                if storge_block[i][j]!="":
                    count+=1
                    if count==self.win_c:
                        full_row_number.append(i)
        self.del_line(full_row_number)

    def del_line(self,full_row_list): #删除行
        global storge_block
        a=len(full_row_list)
        self.line_number+=a
        full_row_list.sort(reverse=False)
        self.score+=a*a
        row_number=0
        while full_row_list:
            max_row=max(full_row_list)
            final_row=max_row+row_number
            for i in range(final_row,0,-1):
                for j in range(self.win_c):
                    storge_block[i][j]=storge_block[i-1][j]
            full_row_list.pop()
            row_number+=1
        self.draw_bg()

    def generate_new_block(self):   #随机生成方块
        block_type=random.choice(list(self.blocks.keys()))
        x=int(self.win_c/2)
        y=0
        global one_block
        one_block={
            "block_type":block_type,
            "pos":self.blocks[block_type]["pos"],
            "xy":[x,y]
        } 
        return one_block

    def draw_bg(self):  #绘制背景
        global storge_block   
        for i in range(self.win_r):
            for j in range(self.win_c):  
                if storge_block[i][j]=="":
                    self.draw_cell(j,i)  
                else:
                    block_type=storge_block[i][j]
                    color=self.blocks[block_type]["color"]
                    self.draw_cell(j,i,color)

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
        global storge_block
        if block is None:
            return
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x+direction[0]
            y1=y0+y+direction[1]
            if x1<0 or x1>=self.win_c or y1>=self.win_r :
                return False
            elif y1>=0 and storge_block[y1][x1]:
                return False
            else:
                return True


    def save_block_list(self,block):        #存落地方块位置
        global storge_block
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x
            y1=y0+y 
            storge_block[y1][x1]=block["block_type"]
        self.check_line()

    def move_horizontal(self,event):        #横向移动 
        global one_block
        if one_block is None:
            return
        direction=[0,0]
        if event.keysym=="Left":
            direction=[-1,0]
        elif event.keysym=="Right":
            direction=[1,0]
        else:
            return
        if self.check_move(one_block,direction) and one_block is not None:
            self.block_move(one_block,direction)

    def rotation_block(self,event): #旋转方块
        global storge_block
        global one_block
        if one_block is None or one_block["block_type"]=="O":
            return
        
        if event.keysym=="Up":
            old_block={"xy":one_block["xy"],"pos":one_block["pos"],"block_type":one_block["block_type"]}
            x,y=one_block["xy"]
            rotation_list=[]
            for x1,y1 in one_block["pos"]:
                x2=y1
                y2=-x1
                xx=x+x2
                yy=y+y2
                if xx<0 or xx>=self.win_c or storge_block[yy][xx]:
                    return
                rotation_list.append([x2,y2])
            new_block=one_block
            new_block["pos"]=rotation_list
            if self.check_move(new_block):
                one_block=new_block
            self.draw_block(old_block,False)
            self.draw_block(one_block,True)
            
    def down_block(self,event):
        global one_block
        global storge_block
        
        if one_block is None:
            return
        if event.keysym=="Down":
            x,y=one_block["xy"]
            i=0
            dis1=[]
            for x1,y1 in one_block["pos"]:
                x2=x+x1
                y2=y+y1
                dis0=0
                for i in range(self.win_r):
                    if storge_block[i][x2]=="":
                        dis0+=1
                    else:
                        break
                
                dis1.append(dis0-y2-1)
            self.block_move(one_block,[0,min(dis1)])
            self.save_block_list(one_block)
            self.generate_new_block()
                
            
win=tk.Tk() 
tetris=Tetris(win)
win.mainloop()
