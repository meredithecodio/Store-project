class Product:
    def __init__(self, productid, name, category, price, quantity):
        self.productid = productid
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.productid] = product

    def update_stock(self, productid, quantity):
        if productid in self.products:
            self.products[productid].quantity = quantity

    def get_product_info(self, productid):
        if productid in self.products:
            return self.products[productid]
        else:
            return None

class Transaction:
    def __init__(self, transactionid, products, quantities):
        self.transactionid = transactionid
        self.products = products
        self.quantities = quantities

    def calculate_total(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.price * quantity
        return total