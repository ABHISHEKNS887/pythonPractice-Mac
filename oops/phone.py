from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Calling super function to have access to all function / methods from parent class
        super().__init__(
            name, price, quantity
        )
        # Run validation to received arguments
        assert broken_phones >= 0, f"Broken {broken_phones} is not greater or equal to than zero"

        # Assign to self object
        self.broken_phones = broken_phones

    def calculate_price(self):
        quantity = (self.quantity - self.broken_phones)
        return self.price * quantity
