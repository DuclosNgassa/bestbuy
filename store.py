from products import Product


class Store:

    def __init__(self, products: list[Product]) -> None:
        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the store.
        :param product:
        :return: None
        """
        if product not in self.products:
            self.products.append(product)
        else:
            index_existing_product = self._get_product_index(product.name)
            existing_product = self.products[index_existing_product]
            existing_product.quantity = existing_product.quantity + product.quantity
            self.products[index_existing_product] = existing_product

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from the store based on the quantity of the product.
        :param product: the product to be removed.
        Throw exception if the product is not in the store.
        """
        existing_product = self._find_product(product.name)
        if not existing_product:
            raise Exception(f"Product {product.name} not in store")

        index_existing_product = self._get_product_index(product.name)
        existing_product = self.products[index_existing_product]
        new_quantity = existing_product.quantity - product.quantity
        if new_quantity < 0:
            self.products.remove(product)
        else:
            existing_product.quantity = new_quantity
            self.products[index_existing_product] = existing_product

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum([product.quantity for product in self.products])

    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.active]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        :param shopping_list:
        :return: the total price of the order.
        """
        total_price = 0

        for product, quantity in shopping_list:
            product_in_store = self._find_product(product.name)
            if not product_in_store:
                print(f"Product {product.name} not in store")

            elif quantity > product_in_store.quantity:
                print(
                    f"Sorry we do not have enough items of the product {product.name} in store. We could only deliver {product_in_store.quantity} items.")
            else:
                total_price += product_in_store.buy(quantity)

        return total_price

    def _find_product(self, product_name: str) -> Product | None:
        return next((p for p in self.products if p.name == product_name), None)

    def _get_product_index(self, product_name: str) -> int:
        product_index = next((i for i, p in enumerate(self.products) if p.name == product_name), None)

        if product_index is None:
            raise Exception(f"Product {product_name} not in store")
        return product_index
