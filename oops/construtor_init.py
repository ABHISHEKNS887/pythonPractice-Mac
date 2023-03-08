class Item:
    pay_rate = 0.8  # Class level attribute (The pay rate after 20per discount)

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item('phone', 100)
item1.apply_discount()
print(item1.price)


item2 = Item('laptop', 1000, 40)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# print(Item.__dict__)  # All attributes for class level
# print(item1.__dict__)  # All attributes for instance level
