"""Lab 06 regression checks; fixtures use temporary files only."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from inventory import Inventory
from inventory_manager import main
from inventory_storage import load_inventory, save_inventory
from product import Product


class InventoryTests(unittest.TestCase):
    def test_stock_validation_and_read_only_properties(self):
        product = Product("p001", "Laptop", 1200, 15)
        for value in (-1, 1.5, True, "10"):
            with self.assertRaises(ValueError):
                product.update_stock(value)
            self.assertEqual(product.stock, 15)
        with self.assertRaises(AttributeError):
            product.stock = 50
        product.update_stock(0)
        self.assertEqual(product.stock, 0)
        for price in (-1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                Product("P002", "Mouse", price, 1)

    def test_duplicate_and_search(self):
        inventory = Inventory()
        original = Product("P001", "Laptop", 1200, 15)
        self.assertTrue(inventory.add_product(original))
        self.assertFalse(inventory.add_product(Product("p001", "Other", 1, 0)))
        self.assertIs(inventory.search_product(" p001 "), original)
        self.assertIsNone(inventory.search_product("missing"))
        self.assertEqual(len(inventory.products), 1)

    def test_persistence_and_invalid_files(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            inventory = load_inventory(path)
            inventory.add_product(Product("P001", "Laptop", 1200, 15))
            self.assertTrue(save_inventory(path, inventory))
            self.assertEqual(load_inventory(path).search_product("P001").stock, 15)
            self.assertEqual(json.loads(path.read_text())["P001"]["Name"], "Laptop")
            self.assertFalse(save_inventory(Path(directory), inventory))
            for invalid in ('{broken', '[]', '{"P001": {}}'):
                path.write_text(invalid)
                with self.assertRaises(ValueError):
                    load_inventory(path)
            path.write_text("")
            self.assertEqual(load_inventory(path).products, ())

    def test_all_menu_actions_and_validation(self):
        inventory = Inventory()
        answers = iter([
            "bad", "1", "2", "", "p004", "", "Monitor",
            "nan", "-1", "299.99", "1.5", "10",
            "2", "P004", "3", "P004", "20",
            "4", "P004", "4", "missing", "5", "6",
        ])
        output = io.StringIO()
        with patch("inventory_manager.load_inventory", return_value=inventory), \
                patch("inventory_manager.save_inventory", return_value=True) as save, \
                patch("builtins.input", side_effect=lambda _: next(answers)), \
                contextlib.redirect_stdout(output):
            main()
        self.assertEqual(inventory.search_product("P004").stock, 20)
        self.assertEqual(len(inventory.products), 1)
        self.assertEqual(save.call_count, 2)
        self.assertIn("Program terminated.", output.getvalue())
        self.assertIn("Product not found.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
