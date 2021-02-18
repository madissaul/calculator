from tkinter import *

expression = ""

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Laskin")
        self.input_text = StringVar()


    def clear_f(self):
        global expression
        expression = ""
        self.input_text.set("")


    def click_f(self,item):
        global expression
        expression = expression + str(item)
        self.input_text.set(expression)

    def equal_f(self):
        global expression
        result = str(eval(expression))
        self.input_text.set(result)
        expression = ""



    def widgets(self):
        self.entry_1 = Entry(self.root, width = 20, textvariable = self.input_text, font = ('arial', 18), borderwidth = 7, justify = "right")
        self.entry_1.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10, ipady = 10)



        #Create buttons in a grid
        self.button_1 = Button(self.root, text = "1", padx = 30, pady = 20, command = lambda: self.click_f(1))
        self.button_2 = Button(self.root, text = "2", padx = 30, pady = 20, command = lambda: self.click_f(2))
        self.button_3 = Button(self.root, text = "3", padx = 30, pady = 20, command = lambda: self.click_f(3))
        self.button_4 = Button(self.root, text = "4", padx = 30, pady = 20, command = lambda: self.click_f(4))
        self.button_5 = Button(self.root, text = "5", padx = 30, pady = 20, command = lambda: self.click_f(5))
        self.button_6 = Button(self.root, text = "6", padx = 30, pady = 20, command = lambda: self.click_f(6))
        self.button_7 = Button(self.root, text = "7", padx = 30, pady = 20, command = lambda: self.click_f(7))
        self.button_8 = Button(self.root, text = "8", padx = 30, pady = 20, command = lambda: self.click_f(8))
        self.button_9 = Button(self.root, text = "9", padx = 30, pady = 20, command = lambda: self.click_f(9))
        self.button_0 = Button(self.root, text = "0", padx = 30, pady = 20, command = lambda: self.click_f(0))
        self.button_clear = Button(self.root, text = "C", padx = 30, pady = 20, command = lambda: self.clear_f())
        self.button_answer = Button(self.root, text = "=", padx = 30, pady = 20, command = lambda: self.equal_f())
        self.button_divide = Button(self.root, text = "/", padx = 30, pady = 20, command = lambda: self.click_f("/"))
        self.button_multiply = Button(self.root, text = "*", padx = 30, pady = 20, command = lambda: self.click_f("*"))
        self.button_plus = Button(self.root, text = "+", padx = 30, pady = 20, command = lambda: self.click_f("+"))
        self.button_minus = Button(self.root, text = "-", padx = 31.5, pady = 20, command = lambda: self.click_f("-"))

        self.button_7.grid(row = 1, column = 0, ipadx = 1)
        self.button_8.grid(row = 1, column = 1, ipadx = 1)
        self.button_9.grid(row = 1, column = 2, ipadx = 1)

        self.button_4.grid(row = 2, column = 0, ipadx = 1)
        self.button_5.grid(row = 2, column = 1, ipadx = 1)
        self.button_6.grid(row = 2, column = 2, ipadx = 1)

        self.button_1.grid(row = 3, column = 0, ipadx = 1)
        self.button_2.grid(row = 3, column = 1, ipadx = 1)
        self.button_3.grid(row = 3, column = 2, ipadx = 1)


        self.button_0.grid(row = 4, column = 1, ipadx = 1)

        self.button_clear.grid(row = 1, column = 3, ipadx = 1, sticky = E)
        
        self.button_plus.grid(row = 2, column = 3, ipadx = 1, sticky = E)

        self.button_minus.grid(row = 3, column = 3, ipadx = 1, sticky = E)

        self.button_answer.grid(row = 4, column = 3, ipadx = 1, sticky = E)
        self.button_divide.grid(row = 4, column = 0, ipadx = 1)
        self.button_multiply.grid(row = 4, column = 2, ipadx = 1, sticky = E)




    def run(self):
        self.widgets()
        self.root.mainloop()


program = App()

if __name__ == "__main__":
    program.run()