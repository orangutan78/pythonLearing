import tkinter as tk
import random
from PIL import Image,ImageTk


class Tetris:
    '俄罗斯方块'
    FPS=1000                                    #刷新速度
    cell_size=30                                #格子大小
    blocks={
        "O":{"pos":[(-1,-1),(0,-1),(-1,0),(0,0)],"color":["#3e7dff","#2313b9","#160a6f"]},
            "L":{"pos":[(0,-2),(0,-1),(0,0),(1,0)],"color":["#2fe7b9","#0b7b7a","#064141"]},
            "J":{"pos":[(0,-2),(0,-1),(0,0),(-1,0)],"color":["#f29086","#ba483d","#5d150d"]},
            "I":{"pos":[(0,-2),(0,-1),(0,0),(0,1)],"color":["#d2a0eb","#8941af","#4e156b"]},
            "S":{"pos":[(1,-1),(0,-1),(0,0),(-1,0)],"color":["#e3ab89","#aa6237","#663112"]},
            "Z":{"pos":[(-1,-1),(0,-1),(0,0),(1,0)],"color":["#deea00","#8f9600","#363900"]},
            "T":{"pos":[(-1,0),(0,0),(1,0),(0,1)],"color":["#ef99e0","#a53a92","#611353"]}}
    
    
    def __init__(self,parent):                  #构造函数
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
        img=Image.open("./orangutan/img/cry.jpg")
        self.photo=ImageTk.PhotoImage(img)
        self.game_loop()

    def game_loop(self):                        #循环
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
            self.canvas.delete("all")
            self.canvas.create_image(self.canvas.winfo_reqwidth()/2,self.photo.height()/2,image=self.photo)
            self.canvas.create_text(self.canvas.winfo_reqwidth()/2,self.photo.height()+50,text="GAME OVER",fill="RED",font=("微软雅黑",30))
            self.parent.unbind("<KeyPress-Down>")

    def difficult(self):                        #方块掉落速度变更
        if self.line_number==0:
            self.FPS=1000
        else:
            self.FPS =1000//self.line_number
        
    def check_game_over(self):                  #游戏结束
        global storge_block
        for i in storge_block[0]:
            if i:
                return True
        return False

    def check_line(self):                       #检查哪行满
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

    def del_line(self,full_row_list):           #删除行
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

    def generate_new_block(self):               #随机生成方块
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

    def draw_bg(self):                          #绘制背景
        global storge_block   
        for i in range(self.win_r):
            for j in range(self.win_c):  
                if storge_block[i][j]=="":
                    self.draw_bg_cell(j,i) 
                elif storge_block[i][j]:
                    block_type=storge_block[i][j]
                    color=self.blocks[block_type]["color"]
                    self.draw_block_cell(j,i,color)
                
               
    def draw_block_cell(self,x,y,color):        #绘制一个格子
        x1=x*self.cell_size
        x2=x*self.cell_size+5
        x3=x*self.cell_size+25
        x4=x*self.cell_size+30
        y1=y*self.cell_size
        y2=y*self.cell_size+5
        y3=y*self.cell_size+25
        y4=y*self.cell_size+30
        self.canvas.create_polygon(x1,y4,x1,y1,x4,y1,x3,y2,x2,y2,x2,y3,fill=color[0],width=0)
        self.canvas.create_rectangle(x2,y2,x3,y3,fill=color[1],width=0)
        self.canvas.create_polygon(x4,y1,x4,y4,x1,y4,x2,y3,x3,y3,x3,y2,fill=color[2],width=0) 

    def draw_bg_cell(self,x,y):                 #画背景格子
        x1=x*self.cell_size
        x2=x*self.cell_size+30
        y1=y*self.cell_size
        y2=y*self.cell_size+30
        self.canvas.create_rectangle(x1,y1,x2,y2,fill="#333333",outline="#444444",width=2)

    def draw_block(self,block,is_block):        #画方块
        x,y=block["xy"]
        block_type=block["block_type"]
        if is_block==True:
            color=self.blocks[block_type]["color"]
            for i in range(4):
                x0=block["pos"][i][0]+x
                y0=block["pos"][i][1]+y
                self.draw_block_cell(x0,y0,color)
        else:
            for i in range(4):
                x0=block["pos"][i][0]+x
                y0=block["pos"][i][1]+y
                self.draw_bg_cell(x0,y0)
            
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
        return True

    def save_block_list(self,block):            #存落地方块位置
        global storge_block
        x0,y0=block["xy"]
        for x,y in block["pos"]:
            x1=x0+x
            y1=y0+y 
            storge_block[y1][x1]=block["block_type"]
        self.check_line()

    def move_horizontal(self,event):            #横向移动 
        global one_block
        if one_block is None:
            return
        direction=[0,0]
        if event.keysym=="Left":
            direction=[-1,0]
        elif event.keysym=="Right":
            direction=[1,0]
        #else:
          #  return
        if self.check_move(one_block,direction) and one_block is not None:
            self.block_move(one_block,direction)

    def rotation_block(self,event):             #旋转方块
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
            
    def down_block(self,event):                 #Down键加速
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
