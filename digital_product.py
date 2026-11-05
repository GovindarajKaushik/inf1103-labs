"""Products delivered as digital downloads."""
import math

from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 download_size: float):
        super().__init__(product_id, name, price, stock)
        if (isinstance(download_size, bool) or not isinstance(download_size, (int, float))
                or not math.isfinite(download_size) or download_size < 0):
            raise ValueError("Download size must be finite and non-negative.")
        self.__download_size = float(download_size)

    @property
    def download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self.download_size:g} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally through a download."
