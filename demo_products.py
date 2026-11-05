"""Run the Lab 7 product examples outside the class definitions."""
from digital_product import DigitalProduct
from physical_product import PhysicalProduct


def main():
    physical = PhysicalProduct("P001", "Guitar", 250.0, 5, 3.5)
    digital = DigitalProduct("D001", "Music software", 49.0, 20, 850.0)
    physical.display_information()
    digital.display_information()


if __name__ == "__main__":
    main()
