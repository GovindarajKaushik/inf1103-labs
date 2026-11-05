"""Products that have a physical weight."""
import math

from CanBeShipped import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 weight: float):
        super().__init__(product_id, name, price, stock)
        if (isinstance(weight, bool) or not isinstance(weight, (int, float))
                or not math.isfinite(weight) or weight < 0):
            raise ValueError("Weight must be finite and non-negative.")
        self.__weight = float(weight)

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight:g} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        """Charge $5 per kilogram, rounded to the nearest cent."""
        return round(self.weight * 5.0, 2)
