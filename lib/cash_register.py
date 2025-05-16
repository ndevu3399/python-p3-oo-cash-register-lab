class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.transactions.append({"amount": amount, "quantity": quantity})
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")

    def void_last_transaction(self):
        if not self.transactions:
            return
        last_trans = self.transactions.pop()
        self.total -= last_trans["amount"]
        self.items = self.items[:-last_trans["quantity"]]