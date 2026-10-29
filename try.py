import json
import datetime

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
    def add_product(cls, product_id, price_paid, is_loyal, is_valid, payment_choice, filename="transaction_history.json"):
        if not price_paid.isdigit():
            raise ValueError("Price_paid needs to be entered as a string")
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

        date = datetime.date()
        time = datetime.time()

        

        transaction = cls(transaction_id, product_id, price_paid, original_price, is_loyal, date, time, is_valid, payment_choice)

        list_of_transactions.append(transaction.to_dict())

        with open(filename, "w") as f:
            json.dump(list_of_transactions, f, indent= 4)

        return transaction

    
        
    def dispaly_transaction(self):
        return [self.product_id, self.product_name, self.product_price]

if __name__ == "__main__":
    product1 = Product.add_product("cake", 2.99)
    product1.dispaly_product()

    product2 = Product.add_product("red bull", 1.85)
    product2.dispaly_product()


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