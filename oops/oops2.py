from item import Item
from phone import Phone

item = Item('memory', 400, 5)
item.apply_increment(0.4)

phone = Phone('redmi', 300, 3)
print(phone.calculate_price())


#
# phone1 = Phone('android', 100, 5)
# phone2 = Phone('IOS', 1000, 50, 4)
# print(phone1.calculate_price())
# print(phone2.calculate_price())
#
# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7.0))
