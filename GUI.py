import tkinter as tk
from tkinter import *

text = ""   # Global text string
drinkChoice = ""    # Placeholder for user drink choice input

def press(key):
    global text
    if len(text) < 3:
        text += str(key)
        display.set(text)
    # else:
        # error - too many keys pressed.


def setDrinkChoice():
    return
"""
    global text
    
    if len(text) == 3:  # Validate input length
        if isValidDrinkId(text):    # Validate that the input matches a valid product Id
            if isAvailable(text):   # Verify that selected drink is available
                drinkChoice = text  # Store user input in drinkChoice
                # display scan loyalty screen   # Move to next screen
            else:
                # display error - drink out of stock
        else:
            # display error - invalid entry
    else:
        # display error - invalid entry           
"""

def delete():
    global text
    if len(text) > 0:
        text = text[:-1]    # Remove end character
    display.set(text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Vending Machine Interface")
    root.geometry("400x540")
    root.configure(bg="#d2d8db")

    display = StringVar()
    displayFrame = Frame(root, bg="white")
    displayFrame.pack(fill="both", expand=True)

    displayText = Label(displayFrame, textvariable=display, bg='white', fg='black')
    displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    

    btnFrame = Frame(root, bg="#d2d8db")
    btnFrame.pack(fill="both", expand=True)

    for col in range(3):
        btnFrame.grid_columnconfigure(col, weight=1)

    for row in range(4):
        btnFrame.grid_rowconfigure(row, weight=1)

    btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb", command=lambda: press(1))
    btn1.grid(row=0, column=0, sticky="nsew")
    btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb", command=lambda: press(2))
    btn2.grid(row=0, column=1, sticky="nsew")
    btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb", command=lambda: press(3))
    btn3.grid(row=0, column=2, sticky="nsew")
    btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb", command=lambda: press(4))
    btn4.grid(row=1, column=0, sticky="nsew")
    btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb", command=lambda: press(5))
    btn5.grid(row=1, column=1, sticky="nsew")
    btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb", command=lambda: press(6))
    btn6.grid(row=1, column=2, sticky="nsew")
    btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb", command=lambda: press(7))
    btn7.grid(row=2, column=0, sticky="nsew")
    btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb", command=lambda: press(8))
    btn8.grid(row=2, column=1, sticky="nsew")
    btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb", command=lambda: press(9))
    btn9.grid(row=2, column=2, sticky="nsew")
    btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000", command=lambda: delete())
    btnDel.grid(row=3, column=0, sticky="nsew")
    btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb", command=lambda: press(0))
    btn0.grid(row=3, column=1, sticky="nsew")
    btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430", command=lambda: setDrinkChoice())
    btnEnter.grid(row=3, column=2, sticky="nsew")
    
    
    
    
    root.mainloop()