import csv


class Item:
    pay_rate = 0.8  # Class level attribute (The pay rate after 20per discount)
    all = []  # Fetching all attributes

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to than zero"

        # Assign to self object
        self.__name = name  # __ represent private attribute.
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property  # Property = Read-only decorator. it will throw attribute error if we try to overwrite the name.
    def name(self):
        return self.__name

    @name.setter  # This decorator allow us to over-write a variable if it has read-only access as well.
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('Item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()  # built in method
        elif isinstance(num, int):
            return True
        else:
            return False

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):  # This is Encapsulation. changing the value of price.
        self.__price = self.__price + self.__price * increment_value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"

    # Abstract method - hide unnecessary information from instances.
    def __connect(self, smpt_server):
        pass

    def __body(self):
        return f""" {self.name} {self.quantity} Quantity"""

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__body()
        self.__send()
