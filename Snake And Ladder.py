import turtle
import random
import math
from tkinter import *
w=Tk()
dice1=PhotoImage(file="Dice_1.gif")
dice2=PhotoImage(file="Dice_2.gif")
dice3=PhotoImage(file="Dice_3.gif")
dice4=PhotoImage(file="Dice_4.gif")
dice5=PhotoImage(file="Dice_5.gif")
dice6=PhotoImage(file="Dice_6.gif")
vr=PhotoImage(file="First_Winner.gif")
vr2=PhotoImage(file="Second_Winner.gif")
w.configure(background = 'white')
w.title('SNAKE AND LADDER')
can = Canvas(master = w, width = 800, height = 800)
can.pack(side=LEFT)
jax=-340-60;jay=-340+35

def SnL(ip,p1,p2,p2c,tur):
        if p1==ip:
            tur.goto(p2c)
            if p2==60:
                tur.left(90)
            elif p2==50:
                tur.right(90)
            elif ((p1//10)%2)!=((p2//10)%2):
                tur.left(180)
            return p2
        return ip
def mov(i,p,n):
    for j in range(n):
        p.forward(70)
        i=i+1
        if i==10:
            p.left(90)
        if i==11:
            p.left(90)
        if i==30:
            p.left(90)
        if i==31:
            p.left(90)
        if i==50:
            p.left(90)
        if i==51:
            p.left(90)
        if i==70: 
            p.left(90)
        if i==71:
            p.left(90)
        if i==90:
            p.left(90)
        if i==91:
            p.left(90)
        if i==20:
            p.right(90)
        if i==21:
            p.right(90)
        if i==40:
            p.right(90)
        if i==41:
            p.right(90)
        if i==60:
            p.right(90)
        if i==61:
            p.right(90)
        if i==80:
            p.right(90)
        if i==81:
            p.right(90)
        if i==100:
            break

#ladder function
def L(slc,p1,p2,p1cx,p1cy,p2cx,p2cy):
    slc=turtle.RawTurtle(can)
    slc.shape('arrow')
    slc.pensize(3)
    slc.speed(200)
    slc.penup()
    slc.color('red')
    slc.goto(jax+(70*p1cx),jay+(70*p1cy))
    slc.pendown()
    p=(((p2cx-p1cx)**2)+((p2cy-p1cy)**2))**(1/2)
    tht=math.degrees(math.atan((p2cy-p1cy)/(p2cx-p1cx)))
    if tht<0:
        tht+=180
    slc.left(tht)
    slc.forward(70*p)
    slc.backward(10)
    slc.right(90)
    for i in range(int((70*p)/20)):
        slc.forward(30)
        slc.right(90)
        slc.forward(10)
        slc.right(90)
        slc.forward(30)
        slc.left(90)
        slc.forward(10)
        slc.left(90)
    slc.penup()
    slc.forward(30)
    slc.left(90)
    slc.pendown()
    slc.forward(70*p)
    slc.hideturtle()
    
#snake function
def S(slc,p1,p2,p1cx,p1cy,p2cx,p2cy):
        slc=turtle.RawTurtle(can)
        slc.shape('arrow')
        slc.speed(100)
        slc.penup()
        slc.goto(jax+30+(70*p1cx),jay+(70*p1cy))
        slc.pendown()
        slc.pensize(10)
        slc.color('#00FF00')
        if p2==60:
                p=1
                tht=90
        elif p2==50:
                p=13**(1/2)
                tht=math.degrees(math.atan(-(3/2)))
        else:
                p=(((p2cx-p1cx)**2)+((p2cy-p1cy)**2))**(1/2)
                tht=math.degrees(math.atan((p2cy-p1cy)/(p2cx-p1cx)))
        if tht>0:
                tht+=180
        slc.left(tht)
        slc.left(5)
        for j in range(int(p*(2.5))):
                for j in range(2):
                        slc.right(30)
                        slc.forward(5)
                        slc.left(30)
                        slc.forward(5)
                slc.left(30)
                slc.forward(5)
                slc.right(30)
                slc.forward(5)
        slc.penup()
        slc.goto(jax+30+(70*p1cx)-10,jay+(70*p1cy))
        slc.pendown()
        slc.pensize(2)
        slc.begin_fill()
        slc.color('#00FF00')
        slc.circle(10)
        slc.end_fill()
        slc.color('#000000')
        slc.penup()
        slc.backward(1)
        slc.left(90)
        slc.forward(17)
        slc.pendown()
        slc.circle(2)
        slc.penup()
        slc.right(180)
        slc.forward(17)
        slc.backward(4)
        slc.right(90)
        slc.forward(4)
        slc.pendown()
        slc.circle(2)
        slc.hideturtle()

#Layout creation
board = turtle.RawTurtle(can)
board.speed(0)
board.shape('turtle')
board.pensize(3)
board.color('blue')
board.penup()
board.goto(-340,-340)
board.pendown()
count=0
for j in range(2):
    for i in range(2):
        for m in range(1,21):
            board.forward(35)
            if(m%2)!=0:
                board.write(((m+1)//2)+(count*20),font=(8))
        board.left(90)
        board.forward(70)
        board.left(90)
        for m in range(1,21):
            board.forward(35)
            if(m%2)!=0:
                board.write(((m+1)//2)+(count*20)+10,font=(8))
        board.right(90)
        board.forward(70)
        board.right(90)
        count+=1
for m in range(1,21):
    board.forward(35)
    if(m%2)!=0:
        board.write(((m+1)//2)+80,font=(8))
board.left(90)
board.forward(70)
board.left(90)
for m in range(1,21):
    board.forward(35)
    if(m%2)!=0:
        board.write(((m+1)//2)+90,font=(8))
board.right(90)
board.forward(70)
board.right(90)
board.right(90)
for j in range(2):
    for i in range(2):
        board.forward(700)
        board.left(90)
        board.forward(70)
        board.left(90)
        board.forward(700)
        board.right(90)
        board.forward(70)
        board.right(90)
board.forward(700)
board.left(90)
board.forward(70)
board.left(90)
board.forward(700)
board.right(90)
board.forward(70)
board.right(90)
board.forward(700)
board.backward(700)
board.right(90)
board.forward(700)
board.hideturtle()

#ladders and snakes:
S(board,74,53,7,7,8,5)
S(board,98,19,3,9,2,1)
S(board,61,60,1,6,1,5)
S(board,34,4,7,3,4,0)
S(board,96,47,5,9,7,4)
S(board,73,50,8,7,10,4)
S(board,84,36,4,8,5,3)
L(board,44,96,4,4,5,9)
L(board,7,56,7,0,5,5)
L(board,12,48,9,1,8,4)
L(board,41,77,1,4,4,7)
L(board,71,92,10,7,9,9)
L(board,22,43,2,2,3,4)
L(board,36,87,5,3,7,8)
S(board,99,78,2,9,3,7)

#movement of player
p=turtle.RawTurtle(can)
p.shape('circle')
p.penup()
px=-390;py=-320
p.goto(px,py)
px=-390;py=-320
k=turtle.RawTurtle(can)
k.shape('circle')
k.fillcolor('yellow')
k.penup()
kx=px;ky=py+30
k.goto(kx,ky)
p.speed(2)
k.speed(2)
u=0;g=0
d2=0;d1=0
ee=Entry(w,width=8,bd=5)
te=Label(w,text='enter the no of players ,1 or 2:', font=("Helvetica", 16),background = 'White',padx=10, pady=10)
tur=1
play1=Label(w,text='player 1:', font=("Helvetica", 16),background = 'White')
play1.pack(side=TOP)
play2=Label(w,text='player 2:', font=("Helvetica", 16),background = 'White')
play2.pack(side=BOTTOM)
def plent():
        global l1,l2,a1,tur,ee,te,but
        pln=int(ee.get())
        te.destroy()
        ee.destroy()
        but.destroy()
        if pln==1 or pln==2:
                def t1():
                        global u,p,px,py,k,kx,ky,g,d1,d2,a1,l1,l2,tur
                        if tur==1:
                                d1=random.randint(1,6)
                                l1.destroy()
                                a1.destroy()
                                if d1==1:
                                        dic=dice1
                                if d1==2:
                                        dic=dice2
                                if d1==3:
                                        dic=dice3
                                if d1==4:
                                        dic=dice4
                                if d1==5:
                                        dic=dice5
                                if d1==6:
                                        dic=dice6
                                l1=Label(w,image=dic,bd=0)
                                l1.pack(side=TOP)
                                
                                if u==95:
                                        if d1<=5:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==99:
                                        if d1<=1:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==98:
                                        if d1<=2:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==97:
                                        if d1<=3:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==96:
                                        if d1<=4:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==94:
                                        if d1<=6:
                                                mov(u,p,d1)
                                                u=u+d1
                                elif u==100:
                                        l2.destroy()
                                        play1.destroy()
                                        play2.destroy()
                                        l1.destroy()
                                        can.destroy()
                                        v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                        v.pack()
                                        
                                        return 0
                                else:
                                        mov(u,p,d1)
                                        u=u+d1
                                if u==100:
                                        l2.destroy()
                                        play1.destroy()
                                        play2.destroy()
                                        l1.destroy()
                                        can.destroy()
                                        v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                        v.pack()
                                        
                                        return 0
                                u=SnL(u,44,96,(px+(70*5),py+(70*9)),p)
                                u=SnL(u,7,56,(px+(70*5),py+(70*5)),p)
                                u=SnL(u,12,48,(px+(70*8),py+(70*4)),p)
                                u=SnL(u,41,77,(px+(70*4),py+(70*7)),p)
                                u=SnL(u,71,92,(px+(70*9),py+(70*9)),p)
                                u=SnL(u,22,43,(px+(70*3),py+(70*4)),p)
                                u=SnL(u,74,53,(px+(70*8),py+(70*5)),p)
                                u=SnL(u,98,19,(px+(70*2),py+(70*1)),p)
                                u=SnL(u,61,60,(px+(70*1),py+(70*5)),p)
                                u=SnL(u,34,4,(px+(70*4),py+(70*0)),p)
                                u=SnL(u,96,47,(px+(70*7),py+(70*4)),p)
                                u=SnL(u,73,50,(px+(70*10),py+(70*4)),p)
                                u=SnL(u,84,36,(px+(70*5),py+(70*3)),p)
                                u=SnL(u,36,87,(px+(70*7),py+(70*8)),p)
                                u=SnL(u,99,78,(px+(70*3),py+(70*7)),p)
                                if d1==6:
                                        d1=random.randint(1,6)
                                        l1.destroy()
                                        if d1==1:
                                                dic=dice1
                                        if d1==2:
                                                dic=dice2
                                        if d1==3:
                                                dic=dice3
                                        if d1==4:
                                                dic=dice4
                                        if d1==5:
                                                dic=dice5
                                        if d1==6:
                                                dic=dice6
                                        l1=Label(w,image=dic,bd=0)
                                        l1.pack(side=TOP)
                                        
                                        if u==95:
                                                if d1<=5:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==99:
                                                if d1<=1:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==98:
                                                if d1<=2:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==97:
                                                if d1<=3:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==96:
                                                if d1<=4:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==94:
                                                if d1<=6:
                                                        mov(u,p,d1)
                                                        u=u+d1
                                        elif u==100:
                                                l2.destroy()
                                                play1.destroy()
                                                play2.destroy()
                                                l1.destroy()
                                                can.destroy()
                                                v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                                v.pack() 
                                                return 0
                                        else:
                                                mov(u,p,d1)
                                                u=u+d1
                                        if u==100:
                                                l2.destroy()
                                                play1.destroy()
                                                play2.destroy()
                                                l1.destroy()
                                                can.destroy()
                                                v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                                v.pack()
                                                return 0 
                                u=SnL(u,44,96,(px+(70*5),py+(70*9)),p)
                                u=SnL(u,7,56,(px+(70*5),py+(70*5)),p)
                                u=SnL(u,12,48,(px+(70*8),py+(70*4)),p)
                                u=SnL(u,41,77,(px+(70*4),py+(70*7)),p)
                                u=SnL(u,71,92,(px+(70*9),py+(70*9)),p)
                                u=SnL(u,22,43,(px+(70*3),py+(70*4)),p)
                                u=SnL(u,74,53,(px+(70*8),py+(70*5)),p)
                                u=SnL(u,98,19,(px+(70*2),py+(70*1)),p)
                                u=SnL(u,61,60,(px+(70*1),py+(70*5)),p)
                                u=SnL(u,34,4,(px+(70*4),py+(70*0)),p)
                                u=SnL(u,96,47,(px+(70*7),py+(70*4)),p)
                                u=SnL(u,73,50,(px+(70*10),py+(70*4)),p)
                                u=SnL(u,84,36,(px+(70*5),py+(70*3)),p)
                                u=SnL(u,36,87,(px+(70*7),py+(70*8)),p)
                                u=SnL(u,99,78,(px+(70*3),py+(70*7)),p)
                                tur=2
                        #for d2
                        elif tur==2:
                                d2=random.randint(1,6)
                                l2.destroy()
                                a1.destroy()
                                if d2==1:
                                        dic=dice1
                                if d2==2:
                                        dic=dice2
                                if d2==3:
                                        dic=dice3
                                if d2==4:
                                        dic=dice4
                                if d2==5:
                                        dic=dice5
                                if d2==6:
                                        dic=dice6
                                l2=Label(w,image=dic,bd=0)
                                l2.pack(side=BOTTOM)
                                if g==95:
                                        if d2<=5:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==99:
                                        if d2<=1:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==98:
                                        if d2<=2:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==97:
                                        if d2<=3:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==96:
                                        if d2<=4:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==94:
                                        if d2<=6:
                                                mov(g,k,d2)
                                                g=g+d2
                                elif g==100:
                                        l1.destroy()
                                        play1.destroy()
                                        play2.destroy()
                                        l2.destroy()
                                        can.destroy()
                                        v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                        v.pack()
                                        return 0
                                else:
                                        mov(g,k,d2)
                                        g=g+d2
                                if g==100:
                                        l1.destroy()
                                        play1.destroy()
                                        play2.destroy()
                                        l2.destroy()
                                        can.destroy()
                                        v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                        v.pack()
                                        return 0
                                g=SnL(g,44,96,(kx+(70*5),ky+(70*9)),k)
                                g=SnL(g,7,56,(kx+(70*5),ky+(70*5)),k)
                                g=SnL(g,12,48,(kx+(70*8),ky+(70*4)),k)
                                g=SnL(g,41,77,(kx+(70*4),ky+(70*7)),k)
                                g=SnL(g,71,92,(kx+(70*9),ky+(70*9)),k)
                                g=SnL(g,22,43,(kx+(70*3),ky+(70*4)),k)
                                g=SnL(g,74,53,(kx+(70*8),ky+(70*5)),k)
                                g=SnL(g,98,19,(kx+(70*2),ky+(70*1)),k)
                                g=SnL(g,61,60,(kx+(70*1),ky+(70*5)),k)
                                g=SnL(g,34,4,(kx+(70*4),ky+(70*0)),k)
                                g=SnL(g,96,47,(kx+(70*7),ky+(70*4)),k)
                                g=SnL(g,73,50,(kx+(70*10),ky+(70*4)),k)
                                g=SnL(g,84,36,(kx+(70*5),ky+(70*3)),k)
                                g=SnL(g,36,87,(kx+(70*7),ky+(70*8)),k)
                                g=SnL(g,99,78,(kx+(70*3),ky+(70*7)),k)
                                if d2==6:
                                        d2=random.randint(1,6)
                                        l2.destroy()
                                        if d2==1:
                                                dic=dice1
                                        if d2==2:
                                                dic=dice2
                                        if d2==3:
                                                dic=dice3
                                        if d2==4:
                                                dic=dice4
                                        if d2==5:
                                                dic=dice5
                                        if d2==6:
                                                dic=dice6
                                        l2=Label(w,image=dic,bd=0)
                                        l2.pack(side=BOTTOM)
                                        if g==95:
                                                if d2<=5:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==99:
                                                if d2<=1:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==98:
                                                if d2<=2:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==97:
                                                if d2<=3:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==96:
                                                if d2<=4:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==94:
                                                if d2<=6:
                                                        mov(g,k,d2)
                                                        g=g+d2
                                        elif g==100:
                                                l1.destroy()
                                                play1.destroy()
                                                play2.destroy()
                                                l2.destroy()
                                                can.destroy()
                                                v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                                v.pack()
                                                return 0
                                        else:
                                                mov(g,k,d2)
                                                g=g+d2
                                        if g==100:
                                                l1.destroy()
                                                play1.destroy()
                                                play2.destroy()
                                                l2.destroy()
                                                can.destroy()
                                                v=Label(w,image=vr,bg='#151c2f');w.configure(background = '#151c2f')
                                                v.pack()
                                                return 0
                                g=SnL(g,44,96,(kx+(70*5),ky+(70*9)),k)
                                g=SnL(g,7,56,(kx+(70*5),ky+(70*5)),k)
                                g=SnL(g,12,48,(kx+(70*8),ky+(70*4)),k)
                                g=SnL(g,41,77,(kx+(70*4),ky+(70*7)),k)
                                g=SnL(g,71,92,(kx+(70*9),ky+(70*9)),k)
                                g=SnL(g,22,43,(kx+(70*3),ky+(70*4)),k)
                                g=SnL(g,74,53,(kx+(70*8),ky+(70*5)),k)
                                g=SnL(g,98,19,(kx+(70*2),ky+(70*1)),k)
                                g=SnL(g,61,60,(kx+(70*1),ky+(70*5)),k)
                                g=SnL(g,34,4,(kx+(70*4),ky+(70*0)),k)
                                g=SnL(g,96,47,(kx+(70*7),ky+(70*4)),k)
                                g=SnL(g,73,50,(kx+(70*10),ky+(70*4)),k)
                                g=SnL(g,84,36,(kx+(70*5),ky+(70*3)),k)
                                g=SnL(g,36,87,(kx+(70*7),ky+(70*8)),k)
                                g=SnL(g,99,78,(kx+(70*3),ky+(70*7)),k)    
                                tur=1
                        if tur==2:
                                if pln==1:
                                        t1()
                                elif pln==2:
                                        a1=Button(w,text='roll',height=5,width=20,command=t1,font=("Helvetica", 16),background = 'White',padx=10, pady=10)
                                        a1.pack(side=RIGHT)
                        elif tur==1:
                                a1=Button(w,text='roll',height=5,width=20,command=t1,font=("Helvetica", 16),background = 'White',padx=10, pady=10)
                                a1.pack(side=RIGHT)
        else:
                ee=Entry(w,width=8,bd=5)
                te=Label(w,text='plz only enter 1 or 2:', font=("Helvetica", 16),background = 'White',padx=10, pady=10)
                but=Button(w,text='enter',command=plent,width=10,height=1,background = 'White',padx=10, pady=10)
                but.pack(side=RIGHT)
                ee.pack(side=RIGHT)
                te.pack(side=RIGHT)
                l1.destroy()
                l2.destroy()
        l1=Label(w,text='0',height=5,background = 'White',padx=10, pady=10)
        l1.pack(side=TOP)
        l2=Label(w,text='0',height=5,background = 'White',padx=10, pady=10)
        l2.pack(side=BOTTOM)
        a1=Button(w,text ='roll',height=1,width=10,command=t1,font=("Helvetica", 16),background = 'White',padx=10, pady=10)
        a1.pack(side=RIGHT)
but=Button(w,text='enter',font=("Helvetica", 16),command=plent,width=10,height=1,background = 'White',padx=10, pady=10)
but.pack(side=RIGHT)
ee.pack(side=RIGHT)
te.pack(side=RIGHT)
w.mainloop()
