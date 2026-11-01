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