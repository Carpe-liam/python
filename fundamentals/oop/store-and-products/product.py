class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        self.percent_change = percent_change
        self.is_increased = is_increased
        if is_increased == True:
            self.price += self.price * percent_change
            return self
        else:
            return self

    def print_info(self):
        print(f"Item: {self.name} | Category: {self.category} | Price: ${self.price}")