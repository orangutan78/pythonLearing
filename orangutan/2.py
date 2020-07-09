
from tkinter import *  
root = Tk()  
sb = Scrollbar(root)
sb.pack(side ="left",fill ="y")#fill属性前边文章有介绍X\Y\BOTH
#下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set 
tt = Text(root,yscrollcommand = sb.set)
'''for i in range(1000):
    tt.insert(END,str(i))'''
tt.pack(side ="left",fill ="both")
#下面的这句是关键：指定Scrollbar的command的回调函数是Listbar的yview  
sb.config(command = tt.yview) #用config函数设置属性
root.mainloop()  
