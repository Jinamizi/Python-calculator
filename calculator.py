from tkinter import *
import re

from fraction import to_fraction, is_fraction, to_float

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Calculator")

        #main frame fills entire container, expand if necessary
        self.master.rowconfigure( 0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)
        self.master.geometry("350x200")

        self.outputVar = StringVar()
        self.entry = Entry(self, state = DISABLED, textvariable = self.outputVar)
        self.outputVar.set("0")
        self.entry.grid(row = 0, column = 0,columnspan = 4, sticky = W+E+N+S, padx = 1, pady = 1)

        buttons = ["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+","C","1/X","fr","%"]
        for i in range(len(buttons)):
            button = Button(self, text = buttons[i], width = 10)
            button.config(command = lambda text = buttons[i] : self.process(text))
            button.grid(row = (i // 4) + 1, column = i % 4, sticky = W+E+N+S, padx = 1, pady = 1)
            self.rowconfigure( (i // 4) + 1, weight = 1)
            self.columnconfigure( i % 4, weight = 1)
            
        self.rowconfigure( 0, weight = 3)
        self.columnconfigure( 0, weight = 1)
        
    def process(self, text):
        text_displayed = self.outputVar.get()
        if not re.match("[+-]*[1-9][0-9]*([.][0-9])?[+\-/%*]?", text_displayed):
            self.outputVar.set("0")
        
        if text in "0123456789":
            if text_displayed == "0": #no previous input on display
                self.outputVar.set(text)
            elif not (text == "0" and re.search("[*%+\-/]$", text_displayed)): #ensure a number does not with a 0 
                self.outputVar.set(text_displayed + text)
        elif text == "C":
            self.outputVar.set("0")
        elif text == "1/X":
            if not re.search("[.+/\-%*]$", text_displayed): 
                self.outputVar.set(1/eval(text_displayed)) #inverse the number
        elif text == "=":
            if not re.search("[.+/\-%*]$", text_displayed):
                try:
                    self.outputVar.set(eval(text_displayed))
                except Exception as e: #i dont if there can be an exception
                    self.outputVar.set(e)
        elif text in '+-%/*' : #signs
            if not re.search("[.+/\-%*]$", text_displayed):
                self.outputVar.set(text_displayed + text)
        elif text == "." :
            if not re.search("[0-9]*[.][0-9]*|[.+/\-%*]$", text_displayed): #ensure a number do not get two decimals ans a decimal does not come after a sign
                self.outputVar.set(text_displayed + text)
        elif text == "fr": #convert to fraction
            if not re.search("[.+/\-%*]$", text_displayed): #the number does not end with a sign
                if is_fraction(text_displayed): #check if the number is a fraction
                    self.outputVar.set(str(to_float(to_fraction(text_displayed))))
                else:
                    self.outputVar.set(str(to_fraction(text_displayed)))
            

def main():
    Calculator().mainloop()

if __name__ == "__main__":
    main()
