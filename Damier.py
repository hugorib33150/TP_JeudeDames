from tkinter import *

class Damier():
    def __init__(self,canevas):
        self.can = canevas
        
    def start(self):
        coul = "white"
        start_black = True
        for y in range(0, 800, 80):
            if start_black:
                init_x = 0
                
            else:
                init_x = 80
                
            for x in range(init_x, 800, 160):
                self.can.create_rectangle(x,y,x+80,y+80,fill=coul)
                
            start_black = not start_black
            
    def pointeur(self,event):
        x = event.x
        y = event.y
        posx = event.x // 40
        posy = event.y // 40
        print(event.x, event.y)
        print(posx, posy)
        self.can.create_oval(posx*40,posy*40,x+20,y+20,fill='white')       
    

fen1 = Tk()
fen1.geometry("800x800")
can1 = Canvas(fen1,bg='dark grey',height=800,width=800)
can1.pack()

d1 = Damier(can1)
d1.start()

can1.bind("<Button-1>", d1.pointeur)