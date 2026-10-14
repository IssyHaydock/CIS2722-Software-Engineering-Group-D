import json

class Product:
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price
        }

    @classmethod
    def add_product(cls, product_name, product_price, filename="product.json"):
        product_name = product_name.strip()
        product_price = float(product_price)

        if not product_name:
            raise ValueError("product name can not be empty")

        if product_price < 0:
            raise ValueError("product price can not be negative")

        try:
            with open(filename, "r") as f:
                inventory = json.load(f)

        except FileNotFoundError:
            inventory = []

        except json.JSONDecodeError:
            inventory = []

        highest_id = 0

        for saved_products in inventory:
            saved_id = saved_products.get("product_id", "")

            if isinstance(saved_id, str) and len(saved_id) == 3 and saved_id.isdigit():
                highest_id = max(highest_id, int(saved_id))

        next_id =highest_id + 1

        product_id = f"{next_id:03d}"

        product = cls(product_id, product_name, product_price)

        inventory.append(product.to_dict())

        with open(filename, "w") as f:
            json.dump(inventory, f, indent= 4)

        return product

    @classmethod
    def search_product(cls, product_id, filename="product.json"):
        product_id = str(product_id).strip()

        if len(product_id) != 3 or not product_id.isdigit():
            raise ValueError("please enter a correect ID")

        try:
            with open(filename, "r") as f:
                inventory = json.load(f)

        except FileNotFoundError:
            return None

        except json.JSONDecodeError:
            return None

        for saved_products in inventory:
            saved_id = saved_products.get("product_id")

            if saved_id == product_id:
                return cls(
                    saved_products["product_id"],
                    saved_products["product_name"],
                    saved_products["product_price"]
                )
        return None
        
    def dispaly_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product name: {self.product_name}")
        print(f"Product price: £{self.product_price}")

if __name__ == "__main__":
    product1 = Product.add_product("latte", 2.99)
    product1.dispaly_product()

    product2 = Product.add_product("Monster", 1.85)
    product2.dispaly_product()

    inputed_id = input("please enter an id")
    completed_id_search = Product.search_product(inputed_id)

    if completed_id_search is not None:
        completed_id_search.dispaly_product()
    else:
        print("Product Not Found")
