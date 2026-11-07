import inventory_system_copy
import GUI
from GUI import *
import tkinter as tk
from tkinter import *

transaction_data = {
        'product_id': "",
        'price_paid': 0.0,
        'is_loyal': False,
        'is_valid': False,
        'payment_choice': "",
        'final_price_pence': 0
}

valid_loyalty_cards = ["10001", "10002", "10003", "10004", "10005"]

available_change = {
    200: 5,   # £2 coins
    100: 10,  # £1 coins
    50: 8,    # 50p coins
    20: 10,   # 20p coins
    10: 15    # 10p coins
}

valid_cash_values = [10,20,50,100,200,500,1000]  # Valid cash values in pence

# Check if the product ID is valid
def is_valid_product_id(product_id):
    try:
        found_product = inventory_system_copy.Product.search_product(product_id)
        if found_product is not None:
            return True
        else:
            return False
    except ValueError:
        return False


# Calculate the final price based on loyalty status
def calculate_final_price():
    product_id = transaction_data["product_id"]

    product = inventory_system_copy.Product.search_product(product_id)

    if product is None:
        raise ValueError("Product not found")

    price_pence = round(product.product_price * 100)

    if transaction_data["is_loyal"]:
        final_price = round(price_pence * 0.90)
    else:
        final_price = price_pence

    transaction_data["final_price_pence"] = final_price

    return final_price


# Test cases
# print(calculate_final_price("001", True))  # Example usage for a loyal customer
# print(calculate_final_price("002", False))  # Example usage for a non-loyal customer    

# Validate loyalty status
def validate_loyalty_status(card_id):
    if card_id in valid_loyalty_cards:
        return True
    else:
        return False

# Skip loyalty validation
def skip_loyalty():
    transaction_data["is_loyal"] = False
    calculate_final_price()

def set_payment_choice(choice):
    if choice not in ["cash", "card"]:
        return False

    transaction_data["payment_choice"] = choice
    return True


# Validate cash value
def is_valid_cash_value(cash_value):
    if type(cash_value) is not int:
        return False
    if cash_value in valid_cash_values:
        return True
    else:
        return False
    

# Validate cash payment
def validate_cash_payment(cash_amount, final_price):
    if type(cash_amount) is not int or type(final_price) is not int:
        return False
    if cash_amount < 0 or final_price < 0:
        return False
    
    if cash_amount >= final_price:
        return True
    else:
        return False
    
# Calculate change
def calculate_change(cash_amount, final_price):
    if type(cash_amount) is not int or type(final_price) is not int:
        raise ValueError("Cash amounts must be in whole pence")

    if cash_amount < 0 or final_price < 0:
        raise ValueError("Cash amounts cannot be negative")

    if cash_amount < final_price:
        raise ValueError("Not enough cash inserted")

    return cash_amount - final_price
   


# Check if the machine can give change
def can_give_change(change_needed, available_change):
    if type(change_needed) is not int or change_needed < 0:
        return False, {}
    change_values = sorted(available_change.keys(), reverse=True)
    
    
    def find_change(amount_left, position):
        # All coin values have been checked
        if position == len(change_values):
            if amount_left == 0:
                return {}
            return None

        coin = change_values[position]

        # Maximum number of this coin we can use
        max_coins = min(amount_left // coin, available_change.get(coin, 0))

        # Try different numbers of this coin
        for count in range(max_coins, -1, -1):
            remaining = amount_left - (count * coin)
            result = find_change(remaining, position + 1)

            if result is not None:
                if count > 0:
                    result[coin] = count
                return result

        return None

    coins_to_return = find_change(change_needed, 0)

    if coins_to_return is not None:
        return True, coins_to_return
    else:
        return False, {}
    

# Validate card payment
def validate_card_payment():
    while True:
        answer = input("Was card payment approved by bank? (y/n): ").strip().lower()

        if answer == "y":
            return True

        elif answer == "n":
            return False

        else:
            print("Please enter y or n.")

# Cancel transaction
def cancel_transaction(payment_method, cash_inserted):
    if payment_method == "cash" and cash_inserted > 0:
        return f"Transaction cancelled. Returning cash: £{cash_inserted / 100:.2f}"

    elif payment_method == "cash":
        return "Transaction cancelled. No cash to return."

    elif payment_method == "card":
        return "Transaction cancelled. No card payment processed."

    else:
        return "Invalid payment method."

# Process purchase
def process_purchase(cash_inserted=0):
    product_id = transaction_data["product_id"]
    payment_method = transaction_data["payment_choice"]
    final_price = transaction_data["final_price_pence"]

    transaction_data["is_valid"] = False
    transaction_data["price_paid"] = 0.0

    if not is_valid_product_id(product_id):
        return "invalid_product"
    
    if final_price <= 0:
        return "invalid_final_price"

    if payment_method == "cash":

        if not validate_cash_payment(cash_inserted, final_price):
            return "insufficient_cash"

        change_needed = calculate_change(cash_inserted, final_price)

        can_return, coins_used = can_give_change(
            change_needed, available_change
        )

        if not can_return:
            return "cannot_return_change"

        for coin, quantity in coins_used.items():
            available_change[coin] -= quantity

        transaction_data["price_paid"] = final_price / 100
        transaction_data["is_valid"] = True

        return "success"

    elif payment_method == "card":

        if not validate_card_payment():
            return "card_declined"

        transaction_data["price_paid"] = final_price / 100
        transaction_data["is_valid"] = True

        return "success"

    return "invalid_payment_method"


def set_drink_choice(choice):
    global transaction_data
    
    if len(choice) == 3:  # Validate input length
        if is_valid_product_id(choice):    # Validate that the input matches a valid product Id
            if is_available(choice):   # CHANGE TO NEW FUNTCION    Verify that selected drink is available
                transaction_data['product_id'] = choice  # Store user input in product_id
                return True
                # Displays scan loyalty screen   # Move to next screen
            else:
                return False
        else:
            return False
    else:
        return False

     
# PLACE HOLDER FUNCTIONS <----------------------------------------------------------------------------------------------------------------------------------------------
def is_available(entry):
    while True:
        answer = input("Is the selected drink available? (y/n): ").lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")    

def is_valid_loyalty(card_id):
    if validate_loyalty_status(card_id):
        transaction_data["is_loyal"] = True
        calculate_final_price()
        return True
    
    transaction_data["is_loyal"] = False
    transaction_data["final_price_pence"] = 0
    return False

def save_transaction():
    inventory_system_copy.Transaction_history.add_transaction(
        transaction_data.copy()
    )

def reset_transaction():
    transaction_data.update({
        "product_id": "",
        "price_paid": 0.0,
        "is_loyal": False,
        "is_valid": False,
        "payment_choice": "",
        "final_price_pence": 0
    })

if __name__ == "__main__":
    # Build GUI    
    root = GUI.App()
    root.title("Vending Machine Interface")
    root.geometry("400x540")


    root.mainloop()