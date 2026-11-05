import main
from main import *
import tkinter as tk
from tkinter import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # Initialise frames to an empty array
        self.frames = {}  
 
        # Iterate through window options
        for F in (MainWindow, LoyaltyWindow, ChoosePaymentWindow, CashPaymentWindow, CardPaymentWindow, OutcomeWindow, AdminWindow):
 
            frame = F(container, self)
 
            # Initialise frames for each option
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(MainWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        admin_btn = Button(displayFrame, text='Admin', fg='black', bg='#a5b1b8', command=lambda: controller.show_frame(AdminWindow))
        admin_btn.place(x=0, y=0)
    
        displayText = Label(displayFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25))
        displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    
        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb", command=lambda: self.press(1))
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb", command=lambda: self.press(2))
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb", command=lambda: self.press(3))
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb", command=lambda: self.press(4))
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb", command=lambda: self.press(5))
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb", command=lambda: self.press(6))
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb", command=lambda: self.press(7))
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb", command=lambda: self.press(8))
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb", command=lambda: self.press(9))
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000", command=lambda: self.delete())
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb", command=lambda: self.press(0))
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430", command=lambda: 
                          (self.reset(), controller.show_frame(LoyaltyWindow)) if main.set_drink_choice(str(self.text)) else None)
        btnEnter.grid(row=3, column=2, sticky="nsew")

    def press(self, key):    
        if len(self.text) < 3:
            self.text += str(key)
            self.display.set(self.text)
    
    
    def delete(self):    
        if len(self.text) > 0:
            self.text = self.text[:-1]    # Remove end character
        self.display.set(self.text)

    def reset(self):
        self.text = ""
        self.display.set(self.text)


class LoyaltyWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        cancelBtn = Button(displayFrame, text='Cancel', bg='#bf0000', fg='white', font=('Arial', 10), command=lambda: 
                           controller.show_frame(MainWindow))
        cancelBtn.place(x=0, y=0)


        centreFrame = Frame(displayFrame, bg='white')
        centreFrame.place(relx=0.5, rely=0.5, anchor='center')
        scanText = Label(centreFrame, text='Enter loyalty card number:', bg='white', fg='black', font=('Arial', 14))   # Else show invalid loyalty error
        scanText.pack(pady=5)
        displayText = Label(centreFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25), width=7, relief='sunken')
        displayText.pack(pady=5)
        skipBtn = Button(centreFrame, text='Skip', bg='#d2d8db', fg='black', font=('Arial', 14), command=lambda: controller.show_frame(ChoosePaymentWindow))
        skipBtn.pack(pady=5)
        
        
        
        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb", command=lambda: self.press(1))
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb", command=lambda: self.press(2))
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb", command=lambda: self.press(3))
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb", command=lambda: self.press(4))
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb", command=lambda: self.press(5))
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb", command=lambda: self.press(6))
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb", command=lambda: self.press(7))
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb", command=lambda: self.press(8))
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb", command=lambda: self.press(9))
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000", command=lambda: self.delete())
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb", command=lambda: self.press(0))
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430", command=lambda: 
                         (self.reset(), controller.show_frame(ChoosePaymentWindow)) if main.is_valid_loyalty() else None)
        btnEnter.grid(row=3, column=2, sticky="nsew")

    def press(self, key):    
        if len(self.text) < 5:
            self.text += str(key)
            self.display.set(self.text)
        # else:
            # error - too many keys pressed.
    
    
    def delete(self):    
        if len(self.text) > 0:
            self.text = self.text[:-1]    # Remove end character
        self.display.set(self.text)

    def reset(self):
            self.text = ""
            self.display.set(self.text)




class ChoosePaymentWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        displayText = Label(displayFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25))
        displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        optionLabel = Label(displayFrame, text='Choose payment method:', bg='white', fg='black')
        optionLabel.pack()
        cashBtn = Button(displayFrame, text='Cash', fg='black', bg='#a5b1b8', command=lambda: controller.show_frame(CashPaymentWindow))
        cashBtn.pack(side='left')
        cardBtn = Button(displayFrame, text='Card', fg='black', bg='#a5b1b8', command=lambda: controller.show_frame(CardPaymentWindow))
        cardBtn.pack(side='right')

        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb")
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb")
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb")
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb")
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb")
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb")
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb")
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb")
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb")
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000")
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb")
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430")
        btnEnter.grid(row=3, column=2, sticky="nsew")


class CashPaymentWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        displayText = Label(displayFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25))
        displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        priceLabel = Label(displayFrame, text='Insert Cash\nPrice: £', bg='white', fg='black')
        priceLabel.pack()

        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb")
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb")
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb")
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb")
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb")
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb")
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb")
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb")
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb")
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000")
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb")
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430")
        btnEnter.grid(row=3, column=2, sticky="nsew")

        #self.after(10000, lambda: self.controller.show_frame(OutcomeWindow))





class CardPaymentWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        displayText = Label(displayFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25))
        displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        priceLabel = Label(displayFrame, text='Tap/Insert card to pay\nPrice: £', bg='white', fg='black')
        priceLabel.pack()

        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb")
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb")
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb")
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb")
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb")
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb")
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb")
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb")
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb")
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000")
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb")
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430")
        btnEnter.grid(row=3, column=2, sticky="nsew")

        #self.after(10000, lambda: self.controller.show_frame(OutcomeWindow))
        


class OutcomeWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)
    
        displayText = Label(displayFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25))
        displayText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.after(200, self.displayOutcome())

        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb")
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb")
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb")
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb")
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb")
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb")
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb")
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb")
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb")
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000")
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb")
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430")
        btnEnter.grid(row=3, column=2, sticky="nsew")

        #self.after(10000, lambda: self.controller.show_frame(MainWindow))

    def displayOutcome(self):
        if transaction_data['is_valid']:
            self.text = "Transaction successful"
            self.display.set(self.text)
        else:
            self.text = "Transaction failed"
            self.display.set(self.text)


class AdminWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.text = ""
    
        self.configure(bg="#d2d8db")
    
        self.display = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)

        returnBtn = Button(displayFrame, text='Back', bg='#bf0000', fg='white', command=lambda: controller.show_frame(MainWindow))
        returnBtn.place(x=0, y=0)

        adminBtnFrame = Frame(displayFrame, bg="white")
        adminBtnFrame.pack(expand=True)

        addBtn = Button(adminBtnFrame, text='Add Product', font=('Arial', 14))
        addBtn.pack()
        removeBtn = Button(adminBtnFrame, text='Remove Product', font=('Arial', 14))
        removeBtn.pack(pady=5)
        
        btnFrame = Frame(self, bg="#d2d8db")
        btnFrame.pack(fill="both", expand=True)
    
        for col in range(3):
            btnFrame.grid_columnconfigure(col, weight=1)
    
        for row in range(4):
            btnFrame.grid_rowconfigure(row, weight=1)
    
        btn1 = Button(btnFrame, text='1', fg="black", bg="#e2e8eb")
        btn1.grid(row=0, column=0, sticky="nsew")
        btn2 = Button(btnFrame, text='2', fg="black", bg="#e2e8eb")
        btn2.grid(row=0, column=1, sticky="nsew")
        btn3 = Button(btnFrame, text='3', fg="black", bg="#e2e8eb")
        btn3.grid(row=0, column=2, sticky="nsew")
        btn4 = Button(btnFrame, text='4', fg="black", bg="#e2e8eb")
        btn4.grid(row=1, column=0, sticky="nsew")
        btn5 = Button(btnFrame, text='5', fg="black", bg="#e2e8eb")
        btn5.grid(row=1, column=1, sticky="nsew")
        btn6 = Button(btnFrame, text='6', fg="black", bg="#e2e8eb")
        btn6.grid(row=1, column=2, sticky="nsew")
        btn7 = Button(btnFrame, text='7', fg="black", bg="#e2e8eb")
        btn7.grid(row=2, column=0, sticky="nsew")
        btn8 = Button(btnFrame, text='8', fg="black", bg="#e2e8eb")
        btn8.grid(row=2, column=1, sticky="nsew")
        btn9 = Button(btnFrame, text='9', fg="black", bg="#e2e8eb")
        btn9.grid(row=2, column=2, sticky="nsew")
        btnDel = Button(btnFrame, text='\u2B8C', fg="white", bg="#bf0000")
        btnDel.grid(row=3, column=0, sticky="nsew")
        btn0 = Button(btnFrame, text='0', fg="black", bg="#e2e8eb")
        btn0.grid(row=3, column=1, sticky="nsew")
        btnEnter = Button(btnFrame, text='\u2713', fg="white", bg="#259430")
        btnEnter.grid(row=3, column=2, sticky="nsew")
                
