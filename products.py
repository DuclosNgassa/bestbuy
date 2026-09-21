from typing import Union


class Product:

    def __init__(self, name: str, price: Union[float, int], quantity: int):
        self._validate_name(name)
        self._validate_price(price)
        self._validate_quantity(quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._validate_name(name)
        self._name = name

    @property
    def price(self) -> float | int:
        return self._price

    @price.setter
    def price(self, price: float | int) -> None:
        self._validate_price(price)
        self._price = price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self._validate_quantity(quantity)
        self._quantity = quantity

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, active: bool) -> None:
        self._active = active

    def show(self):
        print(f"Name: {self._name}, Price: {self._price}, Quantity: {self._quantity}")

    def buy(self, quantity: int) -> float | int:
        if quantity > self._quantity:
            raise Exception(f"Sorry, We do not have enough item in store. You can only order {self._quantity} items")
        self._quantity = (self._quantity - quantity)

        return quantity * self._price

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not name.strip():
            raise ValueError('Name should not be empty')

    def _validate_price(self, price):
        # Prevent booleans (since bool is a subclass of int in Python) and enforce numbers
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError('Price must be a float or int')
        if price < 0:
            raise ValueError('Price must be a positive value')

    def _validate_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer value')
        if quantity < 0:
            raise ValueError('Quantity must be a positive value')
