from tkinter import *
import tkinter.messagebox

click = True
tk = Tk()
frame2 = Tk()
flag = 0
winner = 'none'

#for convert player


def converter(temp_button):
            global click
            if temp_button["text"] == " " and click == True:
             click = False
             temp_button["text"] = "X"
             winner_checker()

            elif temp_button["text"] == " " and click == False:
                click = True
                temp_button["text"] = "O"

                winner_checker()

def winner_checker():

        row()
        column()
        diagonals()


def row():
      global winner
      row1 = default.button1["text"] == default.button2["text"] ==  default.button3["text"] != " "
      row2 = default.button4["text"] == default.button5["text"] == default.button6["text"] != " "
      row3 = default.button7["text"] == default.button8["text"] == default.button9["text"] != " "
      if row1 == True  :
        winner = default.button1["text"]
        tkinter.messagebox._show(" winner :","player "+ default.button1["text"]+" is won")
        frame()

      if row2 == True:
         winner = default.button4["text"]
         tkinter.messagebox._show(" winner :", "player " + winner + " is won")
         frame()

      if row3 == True:
        winner = default.button9["text"]
        tkinter.messagebox._show(" winner :", "player " + winner + " is won")
        frame()




def column():
          global winner
          column1 =  default.button1["text"] == default.button4["text"] == default.button7["text"] != " "
          column2 = default.button2["text"] == default.button5["text"] == default.button8["text"] != " "
          column3 =default.button3["text"] == default.button6["text"] == default.button9["text"] != " "
          if column1 == True :
             winner = default.button1["text"]
             tkinter.messagebox._show(" winner :", "player " +  winner + " is won")
             frame()

          if column2 == True :
            winner = default.button5["text"]
            tkinter.messagebox._show(" winner :", "player " + winner + " is won")
            frame()

          if column3 == True :
             winner = default.button9["text"]
             tkinter.messagebox._show(" winner :", "player " +winner + " is won")
             frame()

def diagonals():
        global winner
        diagonal1 =  default.button1["text"] == default.button5["text"] ==  default.button9["text"] != " "
        diagonal2 = default.button3["text"] ==  default.button5["text"] ==  default.button7["text"] != " "
        if diagonal1 == True :
             winner =  default.button1["text"]
             tkinter.messagebox._show(" winner :", "player " + winner + " is won")
             frame()
        if diagonal2 == True:
            winner = default.button7["text"]
            tkinter.messagebox._show(" winner :", "player " + winner + " is won")
            frame()
def frame():
        frame2.title("winner announcment")
       
        button_reset = Button(frame2, text=" RESET" , font = ( 'times 26 bold' ),height =1, width = 5, command = lambda : reset())
        button_reset.grid(row=1, column=0, sticky= S+N+E+W)
        button_quit = Button(frame2, text=" quit ", font=('times 26 bold'), height=1, width=5, command=lambda: quit())
        button_quit.grid(row=1, column=1, sticky=S+N+E+W)
        frame2.mainloop()

def reset():

    default()

def quit():
      tk.destroy()
      frame2.destroy()

#BOARD
def default():


   
        tk.title("tic tac toe")

        default.button1 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button1))
        default.button1.grid(row=0,column=0,sticky = S+N+E+W)
        default.button2 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button2))
        default.button2.grid(row=0,column=1,sticky = S+N+E+W)
        default.button3 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button3))
        default.button3.grid(row=0,column=2,sticky = S+N+E+W)
        default.button4 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button4))
        default.button4.grid(row=1,column=0,sticky = S+N+E+W)
        default.button5 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button5))
        default.button5.grid(row=1,column=1,sticky = S+N+E+W)
        default.button6 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button6))
        default.button6.grid(row=1,column=2,sticky = S+N+E+W)
        default.button7 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button7))
        default.button7.grid(row=2,column=0,sticky = S+N+E+W)
        default.button8 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button8))
        default.button8.grid(row=2,column=1,sticky = S+N+E+W)
        default.button9 = Button(tk, text=" " , font=('times 26 bold'), height =4, width =5, command = lambda:converter(default.button9))
        default.button9.grid(row=2,column=2,sticky = S+N+E+W)

        tk.mainloop()

default()