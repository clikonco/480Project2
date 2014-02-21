from tkinter import *
import matplotlib.pyplot as plt
import math
import numpy as np
import manhattanknn as mk
import euclidmodule as ek
master = Tk()
master.title("K-Means")
master.geometry("350x425")

Label(master, text="K (# of Clusters)").grid(row=0)
Label(master, text="N (# of Points)").grid(row=1)
Label(master, text="Point 1").grid(row=4)
Label(master, text="Point 2").grid(row=5)
Label(master, text="Point 3").grid(row=6)
Label(master, text="Point 4").grid(row=7)
Label(master, text="Point 5").grid(row=8)
Label(master, text="Point 6").grid(row=9)
Label(master, text="Point 7").grid(row=10)
Label(master, text="Point 8").grid(row=11)
Label(master, text="Point 9").grid(row=12)
Label(master, text="Point 10").grid(row=13)
Label(master, text="Point 11").grid(row=14)
Label(master, text="Point 12").grid(row=15)

    
a = Entry(master) ##width=6,bd=4
b = Entry(master) ##width=6,bd=4
    
a.grid(row=0, column=1)
b.grid(row=1, column=1)

def callback():
    print ("Number of clusters = ",a.get())
    k = a.get()


def callback1():
    print ("Number of points = ",b.get())
    n1 = b.get()
    n = int(n1)


def callback2():
    n1 = b.get()
    n= int(n1)
    if (n>=1):
        x = (e.get())
        y = (f.get())
        plt.plot([x], [y], 'ro')
        if (n>=2):
            x1 = (g.get())
            y1 = (h.get())
            plt.plot([x1],[y1], 'go')
            if(n>=3):
                x2 = (i.get())
                y2 = (j.get())
                plt.plot([x2],[y2],'ro')
                if(n>=4):
                    x3 = (k.get())
                    y3 = (l.get())
                    plt.plot([x3],[y3],'ro')
                    if(n>=5):
                        x4 = (m.get())
                        y4 = (z.get())
                        plt.plot([x4],[y4],'ro')
                        if(n>=6):
                            x5 = (o.get())
                            y5 = (p.get())
                            plt.plot([x5],[y5],'ro')
                            if(n>=7):
                                x6 = (q.get())
                                y6 = (r.get())
                                plt.plot([x6],[y6],'ro')
                                if(n>=8):
                                    x7 = (s.get())
                                    y7 = (t.get())
                                    plt.plot([x7],[y7],'ro')
                                    if(n>=9):
                                        x8 = (u.get())
                                        y8 = (v.get())
                                        plt.plot([x8],[y8],'ro')
                                        if(n>=10):
                                            x9 = (w.get())
                                            y9 = (zz.get())
                                            plt.plot([x9],[y9],'ro')
                                            if(n>=11):
                                                x10 = (aa.get())
                                                y10 = (bb.get())
                                                plt.plot([x10],[y10],'ro')
                                                if(n>=12):
                                                    x11 = (cc.get())
                                                    y11 = (dd.get())
                                                    plt.plot([x11],[y11],'ro')

    plt.axis([0, 20, 0, 20])
    plt.show()


c = Button(master, text="Get K", width=5, command=callback)
c.grid(row=0, column=2)
d = Button(master, text="Get N", width=5, command=callback1)
d.grid(row=1, column=2)

var1 = IntVar()
var2 = IntVar()

def checkbutton_ed():
    if(var1.get()):
        var2.set(0)

def checkbutton_md():
    if(var2.get()):
        var1.set(0)

ED = Checkbutton(master, text="ED", variable=var1, command=checkbutton_ed)
MD = Checkbutton(master, text="MD", variable=var2, command=checkbutton_md)

ED.grid(column=1,row=19)
MD.grid(column=1,row=20)

listbox = Listbox(width=5,height=1,bd=4) ##width=12,height=2,bd=4
listbox.grid(column=1,row=3) 
listbox.insert(END, "    X   ")
listbox = Listbox(width=5,height=1,bd=4) ##width=12,height=2,bd=4
listbox.grid(column=2,row=3) 
listbox.insert(END, "    Y   ")


e = Entry(master) #1 width=3,bd=2
f = Entry(master) 
g = Entry(master) #2
h = Entry(master) 
i = Entry(master) #3
j = Entry(master) 
k = Entry(master) #4
l = Entry(master) 
m = Entry(master) #5
z = Entry(master) 
o = Entry(master) #6
p = Entry(master)
q = Entry(master) #7
r = Entry(master)
s = Entry(master) #8
t = Entry(master)
u = Entry(master) #9
v = Entry(master)
w = Entry(master) #10
zz = Entry(master)
aa = Entry(master) #11
bb = Entry(master)
cc = Entry(master) #12
dd = Entry(master)
 
getxy = Button(master, text="Plot", command=callback2)
getxy.grid(row=17, column=2)
    
e.grid(row=4, column=1, padx=1)
f.grid(row=4, column=2, padx=1)

g.grid(row=5, column=1, padx=1)
h.grid(row=5, column=2, padx=1)

i.grid(row=6, column=1, padx=1)
j.grid(row=6, column=2, padx=1)

k.grid(row=7, column=1, padx=1)
l.grid(row=7, column=2, padx=1)

m.grid(row=8, column=1, padx=1)
z.grid(row=8, column=2, padx=1)

o.grid(row=9, column=1, padx=1)
p.grid(row=9, column=2, padx=1)

q.grid(row=10, column=1, padx=1)
r.grid(row=10, column=2, padx=1)

s.grid(row=11, column=1, padx=1)
t.grid(row=11, column=2, padx=1)

u.grid(row=12, column=1, padx=1)
v.grid(row=12, column=2, padx=1)

w.grid(row=13, column=1, padx=1)
zz.grid(row=13, column=2, padx=1)

aa.grid(row=14, column=1, padx=1)
bb.grid(row=14, column=2, padx=1)

cc.grid(row=15, column=1, padx=1)
dd.grid(row=15, column=2, padx=1)



#importing from Manhattan algorithm
def manhattanalgorithm():    
    listcoord2,listcoord3=mk.manhattan()
    coordx = [float(i[0]) for i in listcoord1]
    coordy = [float(i[1]) for i in listcoord1]
    coordx2 = [float(i[0]) for i in listcoord2]
    coordy2 = [float(i[1]) for i in listcoord2]
    print("Returned Balue from Man: ",coordx,coordy)
    print("Returned Balue 2 from Man: ",coordx2,coordy2)
    plt.plot(coordx,coordy,'ro')
    plt.plot(coordx2,coordy2,'ro')

#importing from Euclid algorithm
def euclidalgorithm():        
    listcoord1,listcoord2,listcoord3=ek.euclidmain()
    print("Returned Balue from Man: ",listcoord1[0],listcoord1[1])
    print("Returned Balue 2 from Man: ",listcoord2[0],listcoord2[1])
    print("Returned Balue 3 from Man: ",listcoord3[0],listcoord3[1])
    plt.plot(listcoord1[0],listcoord1[1],'ro')
    plt.plot(listcoord2[0],listcoord2[1],'ro')
    plt.plot(listcoord3[0],listcoord3[1],'ro')


#euclidalgorithm()

var3 = IntVar()
var4 = IntVar()

##Checkbutton(master, text="Plot", variable=var3).grid(column=2, row=19)
##Checkbutton(master, text="Step", variable=var4).grid(column=2, row=20)

##def step():
##insert ED and MD code
##    if var1 == 1: ## if var1=1, use Euclidean
##
##    else: ## else us Manhattan


step = Button(master, text="Step", command=step)
step.grid(row=20, column=2)

##if var3==true

mainloop()
