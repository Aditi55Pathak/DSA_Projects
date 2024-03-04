class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, price, quantity):
        if item_id in self.inventory:
            print("Item already exists in inventory.")
        else:
            self.inventory[item_id] = {"name": name, "price": price, "quantity": quantity}
            print(f"Item '{name}' added to inventory.")

    def remove_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item removed from inventory.")
        else:
            print("Item not found in inventory.")

    def update_quantity(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id]["quantity"] += quantity
            print("Quantity updated.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item_id, item_details in self.inventory.items():
            print(f"Item ID: {item_id}, Name: {item_details['name']}, Price: {item_details['price']}, Quantity: {item_details['quantity']}")


inventory = Inventory()
inventory.add_item(1, "Keyboard", 20.99, 10)
inventory.add_item(2, "Mouse", 10.99, 15)
inventory.display_inventory()

inventory.update_quantity(1, 5)
inventory.display_inventory()

inventory.remove_item(2)
inventory.display_inventory()
