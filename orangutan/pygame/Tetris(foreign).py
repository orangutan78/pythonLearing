import tkinter as tk
import random
import pygame as pg

class Tetris:
    '俄罗斯方块'
    cell_size=30
    def __init__(self,parent):
        self.parent=parent
        self.canvas=tk.Canvas(root)
        self.canvas.grid(row=0,column=0)
        self.tickrate=1000
        self.parent.after(self.tickrate,self.tick)
        print(self)
        print(self.parent)
    def tick(self):
        print("嘀哒")
        print(self)
        print(self.parent)
        print(self.parent.after)
        #self.parent.after(self.tickrate,self.tick)
    
root=tk.Tk()        
tetris=Tetris(root)
root.mainloop()
