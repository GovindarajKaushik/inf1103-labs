"""Manage a collection of Product objects."""
from product import Product


class Inventory:
    def __init__(self):
        self.__products: dict[str, Product] = {}

    @property
    def products(self) -> tuple[Product, ...]:
        """Return a snapshot without exposing the internal collection."""
        return tuple(self.__products.values())

    def add_product(self, product: Product) -> bool:
        if not isinstance(product, Product):
            raise TypeError("Inventory can only contain Product objects.")
        if product.product_id in self.__products:
            return False
        self.__products[product.product_id] = product
        return True

    def search_product(self, product_id: str) -> Product | None:
        return self.__products.get(product_id.strip().upper())

    def display_all(self) -> None:
        print("\nCurrent Inventory\n" + "-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products.values():
            product.display_information()
        print("-" * 48 + "\n")
