FROM python:3.11-slim

WORKDIR /app/OOP

COPY OOP/*.py OOP/inventory.json ./

CMD ["python", "inventory_manager.py"]
