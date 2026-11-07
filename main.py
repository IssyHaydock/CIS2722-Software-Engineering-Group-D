import inventory_system_copy
import GUI
from GUI import *
import tkinter as tk
from tkinter import *

transaction_data = {
        'product_id': "001",
        'price_paid': 1.50,
        'is_loyal': False,
        'is_valid': False,
        'payment_choice': "card",
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
def calculate_final_price(product_id,is_loyal):
    product_id = transaction_data['product_id']
    product = inventory_system_copy.Product.search_product(product_id)
    if product is None:
        raise ValueError("Product not found")
    
    price_pence = round(product.price * 100)  # Convert to pence
    
    if transaction_data['is_loyal']:
        final_price = round(price_pence * 0.9)  # Apply 10% discount
    else:
        final_price = price_pence  # No discount

    transaction_data["final_price_pence"] = final_price  # Store the final price in transaction_data
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
    bank_response = input("Enter bank response (approved/declined): ").strip().lower()
    if bank_response == "approved":
        return True
    elif bank_response == "declined":
        return False
    else:
        print("Invalid bank response. Please enter 'approved' or 'declined'.")
        return validate_card_payment()  #Ask for valid input

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
def process_purchase(product_id, card_id, payment_method,cash_inserted=0):
    # Validate product ID
    if not is_valid_product_id(product_id):
        return "Invalid product ID."

    # Validate loyalty status
    is_loyal = validate_loyalty_status(card_id)

    # Calculate final price
    final_price_pence = calculate_final_price(product_id, is_loyal)


    if payment_method == "cash":
        # Validate cash payment
        if not validate_cash_payment(cash_inserted, final_price_pence):
            return "Insufficient cash provided."

        # Calculate change needed
        change_needed = calculate_change(cash_inserted, final_price_pence)

        # Check if the machine can give change
        can_change, coins_to_return = can_give_change(change_needed, available_change)
        if not can_change:
            return "Cannot provide change for this transaction."

        return f"Purchase successful. Change to return: {coins_to_return}"

    elif payment_method == "card":
        # Validate card payment
        if not validate_card_payment():
            return "Card payment declined."

        return "Purchase successful with card payment."

    else:
        return "Invalid payment method."
    # Add any additional logic for handling the purchase, updating inventory, etc. after quantity added



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
    return False



if __name__ == "__main__":
    # Build GUI    
    root = GUI.App()
    root.title("Vending Machine Interface")
    root.geometry("400x540")

    """    
    # Example usage
    var1 = inventory_system_copy.Transaction_history.add_transaction(transaction_data)
    product_id = input("Enter product ID: ")
    card_id = input("Enter loyalty card ID (or press Enter if none): ")
    payment_method = input("Enter payment method (cash/card): ").strip().lower()

    cash_inserted = 0
    if payment_method == "cash":
        cash_inserted = int(input("Enter cash amount in pence: "))

    result = process_purchase(product_id, card_id, payment_method, cash_inserted)
    print(result)
    """

    root.mainloop()