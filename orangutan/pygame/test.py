######删除某图形#####
'''
from tkinter import *
def main():
    root = Tk()

    w = Canvas(
        root,
        width=200,
        height=200,
        background="white"
    )
    w.pack()

    y=w.create_line(0, 100, 200, 100, fill='yellow')

    r=w.create_line(100, 0, 100, 200, fill='red', dash=(4, 4))

    t=w.create_rectangle(50, 50, 150, 150, fill='blue')

    b = Button(root,
           text='删除全部',
           command=(lambda x=t: w.delete(t)))
    b.pack()
    w.delete(ALL)
    mainloop()
if __name__ == '__main__':
    main()
'''

'''
tk=tkinter.Tk()
im=tkinter.Image.open()
img=tkinter.PhotoImage(file="orangutan/img/cry.jpg")

img_canvas=tk.Canvas(win,width=self.win_c*self.cell_size,height=self.win_r*self.cell_size)
img_canvas.create_image(image=img)
img_canvas.pack()
'''
'''
from PIL import Image,ImageTk
import tkinter

tk = tkinter.Tk()
img = Image.open("orangutan/img/cry.jpg")
photo = ImageTk.PhotoImage(img)
canvas1=tkinter.Canvas(tk,width=300,height=500,bd=0)
canvas1.create_image(canvas1.winfo_reqwidth()/2,photo.height()/2,image=photo)
canvas1.create_text(canvas1.winfo_reqwidth()/2,photo.height()+30,text="GAME OVER",fill="RED",font=("微软雅黑",50))
canvas1.pack()
canvas1.delete("all")
tkinter.Label(canvas1,image=photo,width=200).pack()
canvas1.create_image(canvas1.winfo_reqwidth()/2,photo.height()/2,image=photo)
canvas1.create_text(canvas1.winfo_reqwidth()/2,photo.height()+30,text="GAME OVER",fill="RED",font=("微软雅黑",50))
#canvas1.pack()
#tk.update()
tk.mainloop()'''
from PIL import Image
img = Image.new('RGB', (256, 256), (255, 255, 255))
img.show()
#img.save('bg.jpg')