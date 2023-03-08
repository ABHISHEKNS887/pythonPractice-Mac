class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


item1 = Item('phone', -100)

item2 = Item('laptop', 1000, 40)

print(item1.calculate_price())
print(item2.calculate_price())
