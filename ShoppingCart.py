class ShoppingCart:
    def __init__(self):
        self.items = []  # list of dicts: {"name":..., "price":..., "qty":...}

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": float(price), "qty": int(qty)})

    def remove_item(self, name):
        for i in range(len(self.items)):
            if self.items[i]["name"] == name:
                self.items.pop(i)
                return True
        return False

    def total_price(self):
        total = 0.0
        for item in self.items:
            total += item["price"] * item["qty"]
        return total


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Milk", 2.5, 2)
    cart.add_item("Bread", 1.8, 1)
    print("Total:", cart.total_price())