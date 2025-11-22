import tkinter as tk

def operator(operation):
    
        #addition
    if operation == "+":
        num1 = int(label.cget("text"))
        label.config(text = str(num1) + " + ")
    #subtraction
    elif operation == "-":
        num1 = int(label.cget("text"))
        label.config(text = str(num1) + " - ")
    #multiplication
    elif operation == "x":
        num1 = int(label.cget("text"))
        label.config(text = str(num1) + " x ")
    #division
    elif operation == "/":
        num1 = int(label.cget("text"))
        label.config(text = str(num1) + " / ")
    #exponents
    elif operation == "^":
        num1 = int(label.cget("text"))
        label.config(text = str(num1) + " ^ ")




def pressed(key):
    current = label.cget("text")
    label.config(text = current + key)  

def calculate(): #  22 + 6 
    #split the text field into different numbers and operators
    text = label.cget("text").split(" ")

    num1 = text[0]
    sign = text[1]
    num2 = text[2]

    if sign == "+":
        ans = int(num1) + int(num2)
    elif sign == "-":
        ans = int(num1) - int(num2)
    elif sign == "x":
        ans = int(num1) * int(num2)
    elif sign == "/":
        ans = int(num1) / int(num2) 
    else:
        ans = int(num1) ** int(num2)           
          

    label.config(text = ans)         
    
#create window
window = tk.Tk()
window.geometry("400x500")  
window.title("Calculator")

#add components
label = tk.Label(window, font = ("Arial", 15), width = 32,  height = 2, padx = 25, pady = 30, bg = "green")
label.grid(row = 0, column = 0, sticky = "EW", columnspan = 3)

frame = tk.Frame(window)
#add buttons
plus = tk.Button(frame, text = "+", command = lambda: operator("+"), width = 8, height = 3,  font = ("Helvetica", 13, "bold"))
plus.grid(row = 0, column = 0)
minus = tk.Button(frame, text = "-", command = lambda: operator("-"), width = 8, height = 3, font = ("Helvetica", 13, "bold"))
minus.grid(row = 0, column = 1)
multiply = tk.Button(frame, text = "x", command = lambda: operator("x"), width = 8, height = 3, font = ("Helvetica", 13, "bold"))
multiply.grid(row = 0, column = 2)
divide = tk.Button(frame, text = "/", command = lambda: operator("/"), width = 8, height = 3, font = ("Helvetica", 13, "bold") )
divide.grid(row = 0, column = 3)
power = tk.Button(frame, text = "^", font = ("Helvetica", 13, "bold"), command = lambda: operator("^"), width = 8, height = 3)
power.grid(row = 2, column = 3)



seven = tk.Button(frame, text = "7", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("7"))
seven.grid(row = 2, column = 0)
eight = tk.Button(frame, text = "8", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("8"))
eight.grid(row = 2, column = 1)
nine = tk.Button(frame, text = "9", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("9"))
nine.grid(row = 2, column = 2)
four = tk.Button(frame, text = "4", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("4"))
four.grid(row = 3, column = 0)
five = tk.Button(frame, text = "5", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("5"))
five.grid(row = 3, column = 1)
six = tk.Button(frame, text = "6", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("6"))
six.grid(row = 3, column = 2)
one = tk.Button(frame, text = "1", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("1"))
one.grid(row = 4, column = 0)
two = tk.Button(frame, text = "2", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("2"))
two.grid(row = 4, column = 1)
three = tk.Button(frame, text = "3", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = lambda: pressed("3"))
three.grid(row = 4, column = 2)

calculate = tk.Button(frame, text = "C", font = ("Helvetica", 13, "bold"), width = 8, height = 3, command = calculate)
calculate.grid(row = 4, column = 3)



frame.grid(row = 2, column = 1)

global num1
global num2
global operation



window.mainloop()

        
        