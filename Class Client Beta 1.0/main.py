#base application
import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import messagebox as msg

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Class Client Beta 1.0")
        self.minsize(500,400)
        self.iconphoto(False, tk.PhotoImage(file='luzismall.png'))

        self.create_button()


    def create_button(self):
        self.btn = ttk.Button(self, text = "Mafs", command = self.choice_box)
        self.btn.grid(column=1, row=1)

        self.btn1 = ttk.Button(self, text = "Engine Nearing", command = self.choice_box1)
        self.btn1.grid(column=1, row=2)

        self.btn2 = ttk.Button(self, text = "Past Brohs", command = self.choice_box2)
        self.btn2.grid(column=1, row=3)

        self.btn3 = ttk.Button(self, text = "Alphabet but complicated", command = self.choice_box3)
        self.btn3.grid(column=1, row=4)

        self.btn4 = ttk.Button(self, text = "Aye Pea Bye Oh", command = self.choice_box4)
        self.btn4.grid(column=1, row=5)

        self.btn5 = ttk.Button(self, text = "Aye Pea Bye Oh Pt.2", command = self.choice_box5)
        self.btn5.grid(column=1, row=6)

        self.btn6 = ttk.Button(self, text = "Darin the Man", command = self.choice_box6)
        self.btn6.grid(column=1, row=7)

        self.btn7 = ttk.Button(self, text = "Advanced Movement", command = self.choice_box7)
        self.btn7.grid(column=1, row=8)

        self.btn8 = ttk.Button(self, text = "Chemist Tree", command = self.choice_box8)
        self.btn8.grid(column=1, row=9)

        self.btn9 = ttk.Button(self, text = "Classroom", command = self.choice_box9)
        self.btn9.grid(column=1, row=11)


    def choice_box(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/gv3cxsgfp2")
    
    def choice_box1(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/auxrivnukr")
    
    def choice_box2(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/gjkywal5bw")
    
    def choice_box3(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/h6mafjbswm")

    def choice_box4(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/ahmtcytjhb")
    
    def choice_box5(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/ahmtcytjhb")

    def choice_box6(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/fc7lyoik75")

    def choice_box7(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/fj4anxlzt3")

    def choice_box8(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","u wanna lern?")

        if answer == True:
            webbrowser.open("https://meet.google.com/lookup/a6lay5ujxr")
    
    def choice_box9(self):
        answer = msg.askyesnocancel("Class Client Beta 1.0","enter classroom?")

        if answer == True:
            webbrowser.open("https://classroom.google.com/h")

window = Window()
window.mainloop()