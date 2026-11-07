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

        if hasattr(frame, "on_show"):
            frame.on_show()


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

        centreFrame = Frame(displayFrame, bg='white')
        centreFrame.place(relx=0.5, rely=0.5, anchor='center')
        selectLabel = Label(centreFrame, text='Select Drink:', bg='white', fg='black', font=('Arial', 14))
        selectLabel.pack()
        displayText = Label(centreFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 25), width=4, relief='sunken')
        displayText.pack(pady=2)
        
    
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
                        controller.show_frame(LoyaltyWindow) if main.set_drink_choice(str(self.text)) else None)
        btnEnter.grid(row=3, column=2, sticky="nsew")

    def press(self, key):    
        if len(self.text) < 3:
            self.text += str(key)
            self.display.set(self.text)
    
    
    def delete(self):    
        if len(self.text) > 0:
            self.text = self.text[:-1]    # Remove end character
        self.display.set(self.text)

    def on_show(self):
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
        skipBtn = Button(centreFrame, text='Skip', bg='#d2d8db', fg='black', font=('Arial', 14), command=lambda: [main.skip_loyalty(), controller.show_frame(ChoosePaymentWindow)])
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
                        controller.show_frame(ChoosePaymentWindow) if main.is_valid_loyalty(self.text) else None)
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

    def on_show(self):
            self.text = ""
            self.display.set(self.text)




class ChoosePaymentWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)
    
        self.configure(bg="#d2d8db")

        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)

        cancelBtn = Button(displayFrame, text='Cancel', bg='#bf0000', fg='white', font=('Arial', 10), command=lambda: 
                        controller.show_frame(MainWindow))
        cancelBtn.place(x=0, y=0)

        optionLabel = Label(displayFrame, text='Choose payment method:', bg='white', fg='black', font=('Arial', 14))
        optionLabel.pack()

        centreFrame = Frame(displayFrame, bg='white')
        centreFrame.place(relx=0.5, rely=0.5, anchor='center')
        cashBtn = Button(centreFrame, text='Cash', fg='black', bg='#d2d8db', width=12, height=6,
                        font=('Arial', 14), command=lambda: [main.set_payment_choice("cash"), controller.show_frame(CashPaymentWindow)])
        cashBtn.pack(side='left', padx=20)
        cardBtn = Button(centreFrame, text='Card', fg='black', bg='#d2d8db', width=12, height=6,
                        font=('Arial', 14), command=lambda: [main.set_payment_choice("card"), controller.show_frame(CardPaymentWindow)])
        cardBtn.pack(side='right', padx=20)


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
        self.timer = None
        tk.Frame.__init__(self, parent)
    
        self.configure(bg="#d2d8db")
 
        self.total = 0   
        self.text = ""
        self.display = StringVar()
        self.display.set(self.text)
        self.error = ""
        self.errorDisplay = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)

        cancelBtn = Button(displayFrame, text='Cancel', bg='#bf0000', fg='white', font=('Arial', 10), command=lambda: 
                        self.refund_and_exit())
        cancelBtn.place(x=0, y=0)


        centreFrame = Frame(displayFrame, bg='white')
        centreFrame.place(relx=0.5, rely=1, anchor='s', relwidth=1, relheight=0.85)

        leftFrame = Frame(centreFrame, bg="white")
        leftFrame.pack(side="left", fill="both", expand=True, padx=10)
        priceLabel = Label(leftFrame, text='Insert Cash\nPrice: £', bg='white', fg='black', font=('Arial', 14))
        priceLabel.pack()
        displayText = Label(leftFrame, textvariable=self.display, bg='white', fg='black', font=('Arial', 14))
        displayText.pack()

        displayBtnFrame = Frame(leftFrame, bg='white')
        displayBtnFrame.place(relx=0.5, rely=1, anchor='s', relwidth=0.5, relheight=0.4)
        refundBtn = Button(displayBtnFrame, text='Refund', bg='#d2d8db', fg='black', font=('Arial', 14),
                           command=lambda: self.refund_and_exit())
        refundBtn.pack(side='left', pady=5)
        confirmBtn = Button(displayBtnFrame, text='Confirm', bg='#d2d8db', fg='black', font=('Arial', 14), command=self.confirm_payment()) # show 'Insufficient amount inserted' OR (show transaction successful window AND reset_timer())
        confirmBtn.pack(side='right', pady=5)

        errorTextLabel = Label(leftFrame, textvariable=self.errorDisplay, bg='white', fg='#bf0000', font=('Arial', 14))
        errorTextLabel.pack(pady=2)

        rightFrame = Frame(centreFrame, bg='#d2d8db')
        rightFrame.pack(side='right', fill='y')
        for i in range(4):
            rightFrame.grid_rowconfigure(i, weight=1)

        rightFrame.grid_columnconfigure(0, weight=1)

        val1000 = Button(rightFrame, text="£10", command=lambda: self.increaseAmountPaid(1000))
        val500 = Button(rightFrame, text="£5", command=lambda: self.increaseAmountPaid(500))
        val200 = Button(rightFrame, text="£2", command=lambda: self.increaseAmountPaid(200))
        val100 = Button(rightFrame, text="£1", command=lambda: self.increaseAmountPaid(100))
        val50 = Button(rightFrame, text="50p", command=lambda: self.increaseAmountPaid(50))
        val20 = Button(rightFrame, text="20p", command=lambda: self.increaseAmountPaid(20))
        val10 = Button(rightFrame, text="10p", command=lambda: self.increaseAmountPaid(10))

        val1000.grid(row=0, column=0, sticky="nsew")
        val500.grid(row=1, column=0, sticky="nsew")
        val200.grid(row=2, column=0, sticky="nsew")
        val100.grid(row=3, column=0, sticky="nsew")
        val50.grid(row=4, column=0, sticky="nsew")
        val20.grid(row=5, column=0, sticky="nsew")
        val10.grid(row=6, column=0, sticky="nsew")
    

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

    def increaseAmountPaid(self, value):
        self.total += value
        self.text = "Amount Paid: £" + f"{self.total / 100:.2f}"
        self.display.set(self.text)
        # Validate amount on each call -----------------------------------------------------------------------------------------------------------------------------

    def confirm_payment(self):
        self.reset_timer()

        result = main.process_purchase(self.total)

        if result == "success":
            self.return_change()
            main.save_transaction()

        elif result == "cannot_return_change":
            self.cannot_return_change()
            main.save_transaction()

        elif result == "insufficient_cash":
            self.refund()
            main.save_transaction()

        self.controller.show_frame(OutcomeWindow)
    
    def refund_and_exit(self):
        self.reset_timer()
        self.refund()

        main.transaction_data["is_valid"] = False
        main.transaction_data["price_paid"] = 0.0

        self.controller.show_frame(OutcomeWindow)
            
    def on_show(self):
        self.total = 0
        self.text = "Amount Paid: £0.00"
        self.display.set(self.text)
        self.errorDisplay.set("")

        self.start_timer()

    def start_timer(self):
        self.timer = self.after(120000, 
                        lambda: self.controller.show_frame(OutcomeWindow))

    def reset_timer(self):
        if self.timer:
            self.after_cancel(self.timer)

    def refund(self):
        refunded_amount = self.total
        self.total = 0

        self.text = "Amount Paid: £0.00"
        self.display.set(self.text)

        self.errorDisplay.set(
            f"£{refunded_amount / 100:.2f} refunded"
    )

    def return_change(self):
        change_pence = (
            self.total - main.transaction_data["final_price_pence"]
     )

        self.errorDisplay.set(
            f"£{change_pence / 100:.2f} change returned"
        )
    

    def cannot_return_change(self):
        refunded_amount = self.total
        self.total = 0

        self.display.set("Amount Paid: £0.00")

        self.errorDisplay.set(
            f"Insufficient change available. "
            f"£{refunded_amount / 100:.2f} refunded"
        )




class CardPaymentWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.timer = None
        tk.Frame.__init__(self, parent)
    
        self.configure(bg="#d2d8db")

        self.error = ""
        self.errorDisplay = StringVar()
        displayFrame = Frame(self, bg="white")
        displayFrame.pack(fill="both", expand=True)

        cancelBtn = Button(displayFrame, text='Cancel', bg='#bf0000', fg='white', font=('Arial', 10), command=lambda: 
                        controller.show_frame(MainWindow))
        cancelBtn.place(x=0, y=0)


        centreFrame = Frame(displayFrame, bg='white')
        centreFrame.place(relx=0.5, rely=1, anchor='s', relwidth=1, relheight=0.6)
        priceLabel = Label(centreFrame, text='Tap/Insert card to pay\nPrice: £', bg='white', fg='black', font=('Arial', 14))
        priceLabel.pack()
        errorTextLabel = Label(centreFrame, textvariable=self.errorDisplay, bg='white', fg='#bf0000', font=('Arial', 14))
        errorTextLabel.pack(pady=5)
        payBtn = Button(centreFrame, text='Pay', bg='#d2d8db', fg='black', font=('Arial', 14))  # if valid card payment show OutcomeWindow, else self.show_error()
        payBtn.pack()

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


    def on_show(self):
        self.start_timer()

    def start_timer(self):
        self.timer = self.after(120000, 
                    lambda: self.controller.show_frame(OutcomeWindow))
    
    def reset_timer(self):
        if self.timer:
            self.after_cancel(self.timer)
    
    def show_error(self):
        self.error = "Error: Insufficient funds"
        self.errorDisplay.set(self.error)
        


class OutcomeWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.timer = None
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

    def on_show(self):
        self.start_timer()
    
    def start_timer(self):
        self.timer = self.after(5000, 
                        lambda: self.controller.show_frame(MainWindow))
        
    def reset_timer(self):
        if self.timer:
            self.after_cancel(self.timer)

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
                
