from tkinter import *
main=Tk()

main.resizable(False,False)
main.config(bg="black")
main.turn="x"
main.player1=0
main.player2=0
main.counter=0
def reset():
    one["text"] = ""
    two["text"] = ""
    three["text"] = ""
    four["text"] = ""
    five["text"] = ""
    six["text"] = ""
    seven["text"] = ""
    eight["text"] = ""
    nine["text"] = ""
    main.turn="x"
def win():
    if (one["text"]=="x" and two["text"]=="x" and three["text"]=="x" ) or (four["text"]=="x" and five["text"]=="x" and six["text"]=="x" ) or (seven["text"]=="x" and eight["text"]=="x" and nine["text"]=="x" ):
        return True
    elif (one["text"]=="x" and four["text"]=="x" and seven["text"]=="x" ) or (two["text"]=="x" and five["text"]=="x" and eight["text"]=="x" ) or (three["text"]=="x" and six["text"]=="x" and nine["text"]=="x" ):
        return True
    elif (one["text"]=="x" and five["text"]=="x" and nine["text"]=="x" ) or (three["text"]=="x" and five["text"]=="x" and seven["text"]=="x" ) :
        return True
    elif (one["text"]=="o" and two["text"]=="o" and three["text"]=="o" ) or (four["text"]=="o" and five["text"]=="o" and six["text"]=="o" ) or (seven["text"]=="o" and eight["text"]=="o" and nine["text"]=="o" ):
        return True
    elif (one["text"]=="o" and four["text"]=="o" and seven["text"]=="o" ) or (two["text"]=="o" and five["text"]=="o" and eight["text"]=="o" ) or (three["text"]=="o" and six["text"]=="o" and nine["text"]=="o" ):
        return True
    elif (one["text"]=="o" and five["text"]=="o" and nine["text"]=="o" ) or (three["text"]=="o" and five["text"]=="o" and seven["text"]=="o" ) :
        return True
    else:
        return False
def check():
    if main.turn=="x":
        if win()==True:
            main.player1+=1
            score()
            reset()
        else:
            if main.counter==9:
                reset()
            else:
                main.turn="o"
    else:
        if win() == True:
            main.player2 += 1
            score()
            reset()
        else:
            if main.counter == 9:
                reset()
            else:
                main.turn = "x"
def score():
    space["text"]="player1   "+str(main.player1)+"\nplayer2   "+str(main.player2)
def play1():
    if one["text"]=="":
        one["text"]=main.turn
    main.counter += 1
    check()
def play2():
    if two["text"]=="":
        two["text"]=main.turn
    main.counter += 1
    check()
def play3():
    if three["text"]=="":
        three["text"]=main.turn
    main.counter += 1
    check()
def play4():
    if four["text"]=="":
        four["text"]=main.turn
    main.counter += 1
    check()
def play5():
    if five["text"]=="":
        five["text"]=main.turn
    main.counter += 1
    check()
def play6():
    if six["text"]=="":
        six["text"]=main.turn
    main.counter += 1
    check()
def play7():
    if seven["text"]=="":
        seven["text"]=main.turn
    main.counter += 1
    check()
def play8():
    if eight["text"]=="":
        eight["text"]=main.turn
    main.counter += 1
    check()
def play9():
    if nine["text"]=="":
        nine["text"]=main.turn
    main.counter += 1
    check()

space1=Label(main,text="Welcome to the game",height=3,bg="black",fg="red",font=("helvetical",15,"bold"))
space1.grid(row=0,column=0,columnspan=3)
one=Button(main,text="",bg="blue",fg="black",width=10,height=3,command=play1)
one.grid(row=1,column=0,padx=0,pady=0)
two=Button(main,text="",bg="red",fg="black",width=10,height=3,command=play2)
two.grid(row=1,column=1,padx=0,pady=0)
three=Button(main,text="",bg="yellow",fg="black",width=10,height=3,command=play3)
three.grid(row=1,column=2,padx=0,pady=0)

four=Button(main,text="",bg="purple",fg="black",width=10,height=3,command=play4)
four.grid(row=2,column=0,padx=0,pady=0)
five=Button(main,text="",bg="green",fg="black",width=10,height=3,command=play5)
five.grid(row=2,column=1,padx=0,pady=0)
six=Button(main,text="",bg="brown",fg="black",width=10,height=3,command=play6)
six.grid(row=2,column=2,padx=0,pady=0)

seven=Button(main,text="",bg="pink",fg="black",width=10,height=3,command=play7)
seven.grid(row=3,column=0,padx=0,pady=0)
eight=Button(main,text="",bg="violet",fg="black",width=10,height=3,command=play8)
eight.grid(row=3,column=1,padx=0,pady=0)
nine=Button(main,text="",bg="orange",fg="black",width=10,height=3,command=play9)
nine.grid(row=3,column=2,padx=0,pady=0)

space=Label(main,text="player1   0\nplayer2   0",height=3,bg="black",fg="red",font=("helvetical",15,"bold"))
space.grid(row=4,column=0,columnspan=3)

main.mainloop()