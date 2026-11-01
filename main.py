import inventory_system

valid_loyalty_cards = ["L001", "L002", "L003"]

available_change = {
    200: 5,   # £2 coins
    100: 10,  # £1 coins
    50: 8,    # 50p coins
    20: 10,   # 20p coins
    10: 15    # 10p coins
}

valid_cash_values = [200, 100, 50, 20, 10]

# Check if the product ID is valid
def is_valid_product_id(product_id):
    try:
        found_product = inventory_system.Product.search_product(product_id)
        if found_product is not None:
            return True
        else:
            return False
    except ValueError:
        return False

# # Test cases
# print(is_valid_product_id("001"))  # Example usage
# print(is_valid_product_id("999"))  # Example usage for a non-existent product
# print(is_valid_product_id("abc"))  # Example usage for an invalid product ID
# print(is_valid_product_id("002"))  # Example usage for another valid product


# Function: is_available(product_id):
# 1. Receive the product ID.
# 2. Search for the product using inventory_system.Product.search_product().
# 3. If the product does not exist, return False.
# 4. Check the product's stock quantity.
# 5. If quantity is greater than 0, return True.
# 6. Otherwise, return False.

# Calculate the final price based on loyalty status
def calculate_final_price(product_id,is_loyal):
    product = inventory_system.Product.search_product(product_id)
    if product is None:
        raise ValueError("Product not found")

    price_pence = round(product.product_price * 100)

    if is_loyal:
        discount = 0.10  # 10% discount for loyal customers
        final_price = price_pence * (1 - discount)
    else:
        final_price = price_pence

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
    coins_to_return = {}

    # Check coins from largest to smallest
    coin_values = [200, 100, 50, 20, 10]

    for coin in coin_values:
        coins_used = 0

        # Use this coin while we still need change
        # and the machine has coins available
        while change_needed >= coin and coins_used < available_change[coin]:
            change_needed -= coin
            coins_used += 1

        if coins_used > 0:
            coins_to_return[coin] = coins_used

    if change_needed == 0:
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
    final_price = calculate_final_price(product_id, is_loyal)
    # Convert pounds to pence
    final_price_pence = round(final_price * 100)


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