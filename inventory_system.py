import json
from datetime import datetime 


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
        return [self.product_id, self.product_name, self.product_price]

class Transaction_history:
    def __init__(self, transaction_id, product_id, price_paid, original_price, is_loyal, date, time, is_valid, payment_choice ):
        self.transaction_id = transaction_id
        self.product_id = product_id 
        self.price_paid = price_paid
        self.original_price = original_price
        self.is_loyal = is_loyal
        self.date = date 
        self.time = time 
        self.is_valid = is_valid
        self.payment_choice = payment_choice



    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "product_id": self.product_id,
            "price_paid": self.price_paid,
            "original_price": self.original_price,
            "is_loyal": self.is_loyal,
            "date": self.date,
            "time": self.time,
            "is_valid": self.is_valid,
            "payment_choice": self.payment_choice
        }

    @classmethod
    def add_transaction(cls, product_id, price_paid, is_loyal, is_valid, payment_choice, filename="transaction_history.json"):
        """if not price_paid.isdigit():
            raise ValueError("Price_paid needs to be entered as a string")"""
        if not isinstance(is_loyal, bool):
            raise ValueError("is_loyal needs to be True or False")
        if not isinstance(is_valid, bool):
            raise ValueError("is_valid needs to be true or false")
        
        if payment_choice not in ["card", "cash"]:
            raise ValueError("not appropriote payment choice")
            

        try:
            with open(filename, "r") as f:
                list_of_transactions = json.load(f)

        except FileNotFoundError:
            list_of_transactions = []

        except json.JSONDecodeError:
            list_of_transactions = []

        highest_id = 0

        for saved_transaction in list_of_transactions:
            saved_id = saved_transaction.get("transaction_id", "")

            if isinstance(saved_id, str) and saved_id.isdigit():
                highest_id = max(highest_id, int(saved_id))

        next_id =highest_id + 1

        transaction_id = next_id

        date = datetime.now().strftime("%d/%m/%y")
        time = datetime.now().strftime("%H:%M:%S")
        completed_id_search = Product.search_product(product_id)

        if completed_id_search is not None:
            product_information = completed_id_search.dispaly_product()
            original_price = product_information[2]
        else:
            raise ValueError("please enter a correct id")

        transaction = cls(transaction_id, product_id, price_paid, original_price, is_loyal, date, time, is_valid, payment_choice)

        list_of_transactions.append(transaction.to_dict())

        with open(filename, "w") as f:
            json.dump(list_of_transactions, f, indent= 4)

        return transaction

    
      #transaction_id, product_id, price_paid, original_price, is_loyal, date, time, is_valid, payment_choice  
    def dispaly_transaction(self):
        return [self.transaction_id, self.product_id, self.price_paid, self.original_price, self.is_loyal, self.date, self.time, self.is_valid, self.payment_choice]


if __name__ == "__main__":
    product1 = Product.add_product("cake", 2.99)
    product1.dispaly_product()

    product2 = Product.add_product("red bull", 1.85)
    product2.dispaly_product()

    transaction = Transaction_history.add_transaction("001", "2.75", True, True, "card")
#how to get information on the object from the product class 
    inputed_id = input("please enter an id")
    completed_id_search = Product.search_product(inputed_id)

    if completed_id_search is not None:
        output_info = completed_id_search.dispaly_product()
        print(output_info[0]) #for product id 
        print(output_info[1]) #for product name
        print(output_info[2]) # for product price 
    else:
        print("Product Not Found")
