#import statements
from tkinter import *
from PIL import Image, ImageTk

#setting up
ximage = Image.open(r"C:\\Users\\Aprameya Kannan\\OneDrive\\Pictures\\Screenshots\\x.png")
oimage = Image.open(r"C:\\Users\\Aprameya Kannan\\OneDrive\\Pictures\\Screenshots\\o.png")
root = Tk()
root.geometry("900x1000")
turn = 0
takenA1 = ""
takenA2 = ""
takenA3 = ""
takenB1 = ""
takenB2 = ""
takenB3 = ""
takenC1 = ""
takenC2 = ""
takenC3 = ""

#defining click functions
def funcA1():
    global turn
    global takenA1
    if(takenA1 == ""):
        if (turn % 2 == 0):
            A1.config(image=xphoto)
            takenA1 ="X"
        else:
            A1.config(image=ophoto)
            takenA1 ="O"
        turn+=1 
        check()
def funcA2():
    global turn
    global takenA2
    if(takenA2 == ""):
        if (turn % 2 == 0):
            A2.config(image=xphoto)
            takenA2 ="X"
        else:
            A2.config(image=ophoto)
            takenA2 ="O"
        turn+=1 
        check()
def funcA3():
    global turn
    global takenA3
    if(takenA3 == ""):
        if (turn % 2 == 0):
            A3.config(image=xphoto)
            takenA3 ="X"
        else:
            A3.config(image=ophoto)
            takenA3 ="O"
        turn+=1 
        check()
def funcB1():
    global turn
    global takenB1
    if(takenB1 == ""):
        if (turn % 2 == 0):
            B1.config(image=xphoto)
            takenB1 ="X"
        else:
            B1.config(image=ophoto)
            takenB1 ="O"
        turn+=1 
        check()
def funcB2():
    global turn
    global takenB2
    if(takenB2 == ""):
        if (turn % 2 == 0):
            B2.config(image=xphoto)
            takenB2 ="X"
        else:
            B2.config(image=ophoto)
            takenB2 ="O"
        turn+=1 
        check()
def funcB3():
    global turn
    global takenB3
    if(takenB3 == ""):
        if (turn % 2 == 0):
            B3.config(image=xphoto)
            takenB3 ="X"
        else:
            B3.config(image=ophoto)
            takenB3 ="O"
        turn+=1 
        check()
def funcC1():
    global turn
    global takenC1
    if(takenC1 == ""):
        if (turn % 2 == 0):
            C1.config(image=xphoto)
            takenC1 ="X"
        else:
            C1.config(image=ophoto)
            takenC1 ="O"
        turn+=1 
        check()
def funcC2():
    global turn
    global takenC2
    if(takenC2 == ""):
        if (turn % 2 == 0):
            C2.config(image=xphoto)
            takenC2 ="X"
        else:
            C2.config(image=ophoto)
            takenC2 ="O"
        turn+=1 
        check()
def funcC3():
    global turn
    global takenC3
    if(takenC3 == ""):
        if (turn % 2 == 0):
            C3.config(image=xphoto)
            takenC3 ="X"
        else:
            C3.config(image=ophoto)
            takenC3 ="O"
        turn+=1 
        check()
def check():
    global turn
    global takenA1
    global takenA2
    global takenA3
    global takenB1
    global takenB2
    global takenB3
    global takenC1
    global takenC2
    global takenC3
    if(takenA1=="X" and takenA2 =="X" and takenA3 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenB1=="x" and takenB2 =="X" and takenB3 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenC1=="X" and takenC2=="X" and takenC3=="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA1=="X" and takenB1 =="X" and takenC1 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA2=="X" and takenB2 =="X" and takenC2 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA3=="X" and takenB3 =="X" and takenC3 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA1=="X" and takenB2 =="X" and takenC3 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA3=="X" and takenB2 =="X" and takenC1 =="X"):
        T.config(text="PLAYER ONE WINS!")
    elif(takenA1=="O" and takenA2 =="O" and takenA3 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenB1=="O" and takenB2 =="O" and takenB3 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenC1=="o" and takenC2=="O" and takenC3=="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA1=="O" and takenB1 =="O" and takenC1 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA2=="O" and takenB2 =="O" and takenC2 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA3=="O" and takenB3 =="O" and takenC3 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA1=="O" and takenB2 =="O" and takenC3 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA3=="O" and takenB2 =="O" and takenC1 =="O"):
        T.config(text="PLAYER TWO WINS!")
    elif(takenA1!="" and takenA2 !="" and takenA3 !="" and takenB1 !="" and takenB2 !="" and takenB3 !="" and takenC1!="" and takenC2!="" and takenC3!=""):
        T.config(text="TIE GAME!")
    
#button placements
A1 = Button(root, command=funcA1)
A1.place(x=0,y=0, height="300", width="300")
A2 = Button(root, command=funcA2)
A2.place(x=0,y=300, height="300", width="300")
A3 = Button(root, command=funcA3)
A3.place(x=0,y=600, height="300", width="300")
B1 = Button(root, command=funcB1)
B1.place(x=300,y=0, height="300", width="300")
B2 = Button(root, command=funcB2)
B2.place(x=300,y=300, height="300", width="300")
B3 = Button(root, command=funcB3)
B3.place(x=300,y=600, height="300", width="300")
C1 = Button(root, command=funcC1)
C1.place(x=600,y=0, height="300", width="300")
C2 = Button(root, command=funcC2)
C2.place(x=600,y=300, height="300", width="300")
C3 = Button(root, command=funcC3)
C3.place(x=600,y=600, height="300", width="300")
T = Label(root)
T.place(x=0,y=900, height="100", width="900")
T.config(text="Player One -> X, Player Two -> O")

#defining images
xphoto = ImageTk.PhotoImage(ximage)
ophoto = ImageTk.PhotoImage(oimage)

#main
root.title("TicTacToe")
root.mainloop()