import inventory_system


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
print(calculate_final_price("001", True))  # Example usage for a loyal customer
print(calculate_final_price("002", False))  # Example usage for a non-loyal customer    