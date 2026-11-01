import main

# 1. Test product ID validation
print("\n--- PRODUCT ID TESTS ---")
print("Existing product:", main.is_valid_product_id("001"))
print("Non-existing product:", main.is_valid_product_id("999"))
print("Invalid product ID:", main.is_valid_product_id("abc"))

# 2. Test loyalty cards
print("\n--- LOYALTY CARD TESTS ---")
print("Valid card:", main.validate_loyalty_status("L001"))
print("Invalid card:", main.validate_loyalty_status("L999"))
print("No card:", main.validate_loyalty_status(None))

# 3. Test price calculation
print("\n--- PRICE TESTS ---")
if main.is_valid_product_id("001"):
    print("Normal price:", main.calculate_final_price("001", False))
    print("Loyalty price:", main.calculate_final_price("001", True))
else:
    print("Product 001 not found. Check product.json.")

# 4. Test accepted cash values
print("\n--- CASH VALUE TESTS ---")
print("£2 accepted:", main.is_valid_cash_value(200))
print("£5 accepted:", main.is_valid_cash_value(500))
print("30p rejected:", main.is_valid_cash_value(30))
print("Text rejected:", main.is_valid_cash_value("abc"))

# 5. Test cash payments
print("\n--- CASH PAYMENT TESTS ---")
print("Enough money:", main.validate_cash_payment(200, 150))
print("Not enough money:", main.validate_cash_payment(100, 150))
print("Negative amount:", main.validate_cash_payment(-100, 150))

# 6. Test change calculation
print("\n--- CHANGE CALCULATION TESTS ---")
print("50p change:", main.calculate_change(200, 150))
print("No change:", main.calculate_change(150, 150))

# 7. Test whether change can be given
print("\n--- CHANGE AVAILABILITY TESTS ---")

print("80p change:", main.can_give_change(80, main.available_change))
print("No change needed:", main.can_give_change(0, main.available_change))

test_coins = {
    200: 0,
    100: 0,
    50: 1,
    20: 3,
    10: 0
}

print("60p using three 20p coins:", main.can_give_change(60, test_coins))
print("30p impossible:", main.can_give_change(30, {
    200: 0, 100: 0, 50: 1, 20: 0, 10: 0
}))

# 8. Test cancellation messages
print("\n--- CANCELLATION TESTS ---")
print(main.cancel_transaction("cash", 200))
print(main.cancel_transaction("cash", 0))
print(main.cancel_transaction("card", 0))

# 9. Test purchase processing
print("\n--- PURCHASE TESTS ---")

if main.is_valid_product_id("001"):
    print("Cash purchase:", main.process_purchase("001", None, "cash", 500))
    print("Insufficient cash:", main.process_purchase("001", None, "cash", 10))
    print("Invalid payment method:", main.process_purchase("001", None, "bitcoin"))
else:
    print("Purchase tests skipped because product 001 does not exist.")


print("\n--- CARD PAYMENT TEST ---")
print(main.process_purchase("001", None, "card"))