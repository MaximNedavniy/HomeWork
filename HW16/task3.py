class Product:
    def __init__(self, my_type, name, price):
        self.my_type = my_type
        self.name = name
        self.price = price

    def __repr__(self):
        return repr(self.name)


class ProductStore:
    warehouse = {}
    profit = 0

    def add(self, product, amount):
        if product.name in self.warehouse:
            self.warehouse[product.name]["amount"] += amount
        else:
            self.warehouse[product.name] = {
                "product": product, "amount": amount, "price": round(product.price * 1.3, 2)}

    def set_discount(self, identifier, percent, identifier_type="name"):
        if identifier_type == "name" and percent <= 100 and not percent < 0:
            self.warehouse[identifier]["price"] -= self.warehouse[identifier]["price"] / 100 * percent
        elif identifier_type == "type" and percent <= 100 and not percent < 0:
            for product in self.warehouse:
                if self.warehouse[product]["product"].my_type == identifier:
                    self.warehouse[product]["price"] -= self.warehouse[product]["price"] / 100 * percent
        else:
            raise ValueError

    def sell_product(self, product_name, amount):
        if amount <= self.warehouse[product_name]["amount"] and amount != 0 and not amount < 0:
            self.warehouse[product_name]["amount"] -= amount
            self.profit += self.warehouse[product_name]["price"] * amount
        else:
            raise ValueError

    def get_income(self):
        print(self.profit)

    def get_all_products(self):
        for key, val in self.warehouse.items():
            print(f"{key}-{val['amount']} pcs.")

    def get_product_info(self, product_name):
        return (product_name, self.warehouse[product_name]["amount"])


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
