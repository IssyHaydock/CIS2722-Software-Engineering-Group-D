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

# Test cases
print(is_valid_product_id("001"))  # Example usage
print(is_valid_product_id("999"))  # Example usage for a non-existent product
print(is_valid_product_id("abc"))  # Example usage for an invalid product ID
print(is_valid_product_id("002"))  # Example usage for another valid product