"""Translate inventory objects to and from the Week 5 JSON format."""
import json
from inventory import Inventory
from product import Product


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
            product = Product(product_id, details["Name"], details["Price"], details["Stock"])
        except KeyError as error:
            raise ValueError(f"Missing field for {product_id}: {error}") from error
        if not inventory.add_product(product):
            raise ValueError(f"Duplicate product ID: {product.product_id}")
    return inventory


def save_inventory(inventory_file, inventory: Inventory) -> bool:
    data = {
        p.product_id: {"Name": p.name, "Price": p.price, "Stock": p.stock}
        for p in inventory.products
    }
    try:
        with open(inventory_file, "w", encoding="utf-8") as destination:
            json.dump(data, destination, indent=4, allow_nan=False)
    except OSError:
        return False
    return True
