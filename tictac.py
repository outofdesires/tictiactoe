from array import *
from tkinter import *
from tkinter import messagebox
import time
import random
topp=Tk()
check=random.randint(0,1)
def checkfull(A):
     for i in range(3):
        ch=A[i][0];
        if(ch!=0):
            c=0;
            for j in range(3):
                if(A[i][j]!=ch):
                  c=1
            if(c!=1):
                if(i==0):
                    B1["bg"]="red"
                    B2["bg"]="red"
                    B3["bg"]="red"
                if(i==1):
                    B4["bg"]="red"
                    B5["bg"]="red"
                    B6["bg"]="red"
                if(i==2):
                    B7["bg"]="red"
                    B8["bg"]="red"
                    B9["bg"]="red"
                if(ch==1):
                 return 2
                else:
                 return 3
     for i in range(3):
        ch=A[0][i]
        if(ch!=0):
            c=0;
            for j in range(3):
                if(A[j][i]!=ch):
                  c=1
            if(c!=1):
                if(i==0):
                    B1["bg"]="red"
                    B4["bg"]="red"
                    B7["bg"]="red"
                if(i==1):
                    B2["bg"]="red"
                    B5["bg"]="red"
                    B8["bg"]="red"
                if(i==2):
                    B3["bg"]="red"
                    B6["bg"]="red"
                    B9["bg"]="red"
                if(ch==1):
                 return 2
                else:
                 return 3
     ch=A[0][0]
     cx=0
     cy=0
     for i in range(3):
        if(A[i][i]!=1):
         cx=1
        if(A[i][i]!=2):
         cy=1
     if(cx==0):
         B1["bg"]="red"
         B5["bg"]="red"
         B9["bg"]="red"
         return 2
     else:
         if(cy==0):
          B1["bg"]="red"
          B5["bg"]="red"
          B9["bg"]="red"
          return 3
     cx=0;
     cy=0;
     for i in range(3):
        if(A[i][2-i]!=1):
         cx=1
        if(A[i][2-i]!=2):
         cy=1
     if(cx==0):
         B3["bg"]="red"
         B5["bg"]="red"
         B7["bg"]="red"
         return 2
     else:
         if(cy==0):
              B3["bg"]="red"
              B5["bg"]="red"
              B7["bg"]="red"
              return 3
     for i in range(3):
        for j in range(3):
            if(A[i][j]==0):
                return 1
     print("Draw")
     return 4
rows, cols = (3, 3)
A =  [[0 for i in range(cols)] for j in range(rows)]
B1=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B1))
B2=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B2))
B3=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B3))
B4=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B4))
B5=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B5))
B6=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B6))
B7=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B7))
B8=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B8))
B9=Button(topp,text=" ",font=("Arial",30),height=3,width=6,bg='white',command= lambda:click(B9))
B1.grid(row=0,column=0)
B2.grid(row=0,column=1)
B3.grid(row=0,column=2)
B4.grid(row=1,column=0)
B5.grid(row=1,column=1)
B6.grid(row=1,column=2)
B7.grid(row=2,column=0)
B8.grid(row=2,column=1)
B9.grid(row=2,column=2)
def click(b):
            global check,A,B1,B2,B3,B4,B5,B6,B7,B8,B9
            if(b==B1):
             e=0
             f=0
            if(b==B2):
             e=0
             f=1
            if(b==B3):
             e=0
             f=2
            if(b==B4):
             e=1
             f=0
            if(b==B5):
             e=1
             f=1
            if(b==B6):
             e=1
             f=2
            if(b==B7):
             e=2
             f=0
            if(b==B8):
             e=2
             f=1
            if(b==B9):
             e=2
             f=2
            if(A[e][f]==0):
             if(check==0):
              A[e][f]=1
              b["text"]="X"
              check=1
             else:
              A[e][f]=2
              b["text"]="O"
              check=0
            else:
                if(b==B1):
                 B1.configure(bg="yellow")
                 topp.update()
                 time.sleep(0.2)
                 B1.configure(bg="white")
                if(b==B2):
                 B2["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B2["bg"]="white"
                if(b==B3):
                 B3["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B3["bg"]="white"
                if(b==B4):
                 B4["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B4["bg"]="white"
                if(b==B5):
                 B5["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B5["bg"]="white"
                if(b==B6):
                 B6["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B6["bg"]="white"
                if(b==B7):
                 B7["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B7["bg"]="white"
                if(b==B8):
                 B8["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B8["bg"]="white"
                if(b==B9):
                 B9["bg"]="yellow"
                 topp.update()
                 time.sleep(0.2)
                 B9["bg"]="white"
            if(checkfull(A)==2):
                M=messagebox.askyesno("Result","X won,Want to play again?")
                if(M):
                    reset()
                if(not M):
                    topp.destroy()
            if(checkfull(A)==3):
                M=messagebox.askyesno("Result","O won,Want to play again?")
                if(M):
                    reset()
                if(not M):
                    topp.destroy()
            if(checkfull(A)==4):
                M=messagebox.askyesno("Result","Draw,Want to play again?")
                if(M):
                    reset()
                if(not M):
                    topp.destroy()
def reset():
    global A,B1,B2,B3,B4,B5,B6,B7,B8,B9,check
    rows, cols = (3, 3)
    B1["text"]=" "
    B2["text"]=" "
    B3["text"]=" "
    B4["text"]=" "
    B5["text"]=" "
    B6["text"]=" "
    B7["text"]=" "
    B8["text"]=" "
    B9["text"]=" "
    B1["bg"]="white"
    B2["bg"]="white"
    B3["bg"]="white"
    B4["bg"]="white"
    B5["bg"]="white"
    B6["bg"]="white"
    B7["bg"]="white"
    B8["bg"]="white"
    B9["bg"]="white"
    A =  [[0 for i in range(cols)] for j in range(rows)]
mainloop()
