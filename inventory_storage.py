"""Save and load physical and digital products as JSON."""
import json
from inventory import Inventory
from digital_product import DigitalProduct
from physical_product import PhysicalProduct


def load_inventory(inventory_file) -> Inventory:
    inventory = Inventory()
    try:
        with open(inventory_file, encoding="utf-8") as source:
            contents = source.read()
    except FileNotFoundError:
        return inventory
    data = json.loads(contents) if contents.strip() else {}
    if not isinstance(data, dict):
        raise ValueError("Inventory JSON must be keyed by product ID.")
    for product_id, details in data.items():
        if not isinstance(details, dict):
            raise ValueError(f"Invalid product data for {product_id}.")
        try:
            product_type = details["Type"]
            if product_type == "physical":
                product = PhysicalProduct(product_id, details["Name"], details["Price"],
                                          details["Stock"], details["Weight"])
            elif product_type == "digital":
                product = DigitalProduct(product_id, details["Name"], details["Price"],
                                         details["Stock"], details["DownloadSize"])
            else:
                raise ValueError(f"Unknown product type for {product_id}: {product_type}")
        except KeyError as error:
            raise ValueError(f"Missing field for {product_id}: {error}") from error
        if not inventory.add_product(product):
            raise ValueError(f"Duplicate product ID: {product.product_id}")
    return inventory


def save_inventory(inventory_file, inventory: Inventory) -> bool:
    data = {}
    for product in inventory.products:
        details = {"Name": product.name, "Price": product.price, "Stock": product.stock}
        if isinstance(product, PhysicalProduct):
            details.update({"Type": "physical", "Weight": product.weight})
        elif isinstance(product, DigitalProduct):
            details.update({"Type": "digital", "DownloadSize": product.download_size})
        else:
            raise ValueError(f"Unsupported product type: {type(product).__name__}")
        data[product.product_id] = details
    try:
        with open(inventory_file, "w", encoding="utf-8") as destination:
            json.dump(data, destination, indent=4, allow_nan=False)
    except OSError:
        return False
    return True
