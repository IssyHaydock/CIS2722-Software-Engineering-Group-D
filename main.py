import inventory_system

valid_loyalty_cards = ["L001", "L002", "L003"]

available_change = {
    200: 5,   # £2 coins
    100: 10,  # £1 coins
    50: 8,    # 50p coins
    20: 10,   # 20p coins
    10: 15    # 10p coins
}

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

    base_price = product.product_price

    if is_loyal:
        discount = 0.10  # 10% discount for loyal customers
        final_price = base_price * (1 - discount)
    else:
        final_price = base_price

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


# Validate cash payment
def validate_cash_payment(cash_amount, final_price):
    if cash_amount >= final_price:
        return True
    else:
        return False

# Calculate change
def calculate_change(cash_amount, final_price):
    if cash_amount < final_price:
        raise ValueError("Cash amount is less than the final price")
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
    

